from django.shortcuts import render
from AppCafeReview.models import * 
from AppCafeReview.forms import *
from django.views.generic import ListView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
# Create your views here.

def view_reviews(request): 
    allReviews = Cafeteria.objects.all() #almaceno todas las cafeterías de la base de datos
    return render(request,"AppCafeReview/verReviews.html", {"allReviews": allReviews } ) #guardo todas las cafeterías como un diccionario 

def create_review(request): 
    if request.method == "POST":
 
            miFormulario = CafeteriaFormulario(request.POST)
 
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data #convierte mi formulario en formato diccionario
                  cafeteria = Cafeteria(nombreCafeteria=informacion["nombreCafeteria"], 
                  puntajeCafeteria=informacion["puntajeCafeteria"],
                  puntajeServicio=informacion["puntajeServicio"],
                  puntajeAmbiente=informacion["puntajeAmbiente"],
                  fechaDeVisita=informacion["fechaDeVisita"],
                  comentario=informacion["comentario"], 
                  ) #creamos un objeto de la clase Cafeteria
                  cafeteria.save()
                  return render(request, "AppCafeReview/verReviews.html")
    else:
            miFormulario = CafeteriaFormulario()
 
    return render(request, "AppCafeReview/crearReview.html", {"miFormulario": miFormulario}) #enviamos el formulario al template

def search(request):
    return render(request, "AppCafeReview/buscarReview.html")

def results(request):
    cafeBuscado = request.GET["nombreCafeteria"]
    resultadoCafe=Cafeteria.objects.filter(nombreCafeteria__icontains=cafeBuscado)
    return render(request, "AppCafeReview/resultadoReviews.html",{"cafeBuscado":cafeBuscado, "resultadoCafe":resultadoCafe})

def delete_review(request, reviewer): 
    borrar = Cafeteria.objects.get(reviewer=Cafeteria.nombreReviewer)
    borrar.delete()
    return render(request,"AppCafeReview/crearReview.html" )

def edit_review(request, reviewer):
    editar = Cafeteria.objects.get(reviewer=Cafeteria.nombreReviewer)
    if request.method == 'POST':
        miFormulario = EditarFormulario(request.POST)
        if miFormulario.is_valid():
            editardict=miFormulario.cleaned_data
            editar.reviewer=editardict["reviewer"]
            editar.save()
        else:
            miFormulario=CafeteriaFormulario(initial={"Nopmbre Cafeteria":editar.nombreCafeteria,
                                                      "Puntaje Cafeteria":editar.puntajeCafeteria,
                                                      "Puntaje Servicio":editar.puntajeServicio,
                                                      "Fecha de Visita":editar.fechaDeVisita,
                                                      "Comentario":editar.comentario,
                                                      "Nombre Reviewer":editar.nombreReviewer})
    return render (request, )

def register_user(request):
    if request.method == 'POST':
        miFormulario=UserCreationForm(request.POST)
        if miFormulario.is_valid():
            miFormulario.save()
            return render (request, "AppCafeReview/crearReview.html") 
    else:
        miFormulario=UserCreationForm()
    return render(request,"AppCafeReview/registroUsuario.html", {"miFormulario":miFormulario})
    
def login_user(request):
    if request.method == 'POST':
        miFormulario = AuthenticationForm(request, data = request.POST)
        if miFormulario.is_valid():
            usuario=miFormulario.cleaned_data.GET("username")
            contra=miFormulario.cleaned_data.GET("password")
            miUsuario=authenticate(username=usuario, password=contra)
            if miUsuario:
                login(request, miUsuario)
                return render (request, "AppCafeReview/verReviews.html")
        else:
            mensaje=f"Error. Usuario o contraseña incorrectos"
            return render (request,"AppCafeReview/verReviews.html", {"mensaje": mensaje})
    else:
        miFormulario=AuthenticationForm()
    return render(request, "AppCafeReview/login.html", {"miFormulario":miFormulario})

@login_required
def inicio(request):
    avatares=Avatar.objects.filter(user=request.user.id)
    imagen=avatares[0].avatar.url
    return render(request, "AppCafeReview/inicio.html", {'url': imagen})