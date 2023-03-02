from django.shortcuts import render
from AppCafeReview.models import * 
from AppCafeReview.forms import *
from django.views.generic import ListView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import LogoutView
# Create your views here.

def view_reviews(request): 
    allReviews = Cafeteria.objects.all()
    return render(request,"AppCafeReview/verReviews.html", {"allReviews": allReviews } )

def create_review(request): 
    if request.method == "POST":
 
            miFormulario = CafeteriaFormulario(request.POST)
            print(miFormulario)
 
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data #convierte mi formulario en formato diccionario
                  cafeteria = Cafeteria(nombreCafeteria=informacion["Nombre Cafeteria"], 
                  puntajeCafeteria=informacion["Puntaje Cafeteria"],
                  puntajeServicio=informacion["Puntaje Servicio"],
                  puntajeAmbiente=informacion["Puntaje Ambiente"],
                  fechaDeVisita=informacion["Fecha de Visita"],
                  comentario=informacion["Comentario"], 
                  )
                  cafeteria.save()
                  return render(request, "AppCafeReview/verReviews.html")
    else:
            miFormulario = CafeteriaFormulario()
 
    return render(request, "AppCafeReview/crearReview.html", {"miFormulario": miFormulario})

def search(request):
    return render(request, "AppCafeReview/buscarReview.html")

def results(request):
    cafeBuscado = request.GET["nombreCafeteria"]
    resultadoCafe=Cafeteria.objects.filter(nombreCafeteria__icontains=cafeBuscado)
    return render(request, "AppCafeReview/resultadoReviews.html",{"cafeBuscado":cafeBuscado, "resultadoCafe":resultadoCafe})

def delete_review(request, reviewer): 
    borrar = Cafeteria.objects.get(reviewer=nombreReviewer)
    borrar.delete()
    return render(request,"AppCafeReview/crearReview.html" )

def edit_review(request, reviewer):
    editar = Cafeteria.objects.get(reviewer=nombreReviewer)
    if request.method == 'POST':
        miFormulario = editarFormulario(request.POST)
        if miFormulario.is_valid():
            editardict=miFormulario.cleaned_data
            editar.reviewer=editardict["reviewer"]
            editar.save()
        else:
            pass 
            miFormulario=CafeteriaFormulario(initial={"Nopmbre Cafeteria":editar.nombreCafeteria,
                                                      "Puntaje Cafeteria":editar.puntajeCafeteria,
                                                      "Puntaje Servicio":editar.puntajeServicio,
                                                      "Fecha de Visita":editar.fechaDeVisita,
                                                      "Comentario":editar.comentario,
                                                      "Nombre Reviewer":editar.nombreReviewer})
    return render (request, )

def register_user(request):
    if request.method=='POST':
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