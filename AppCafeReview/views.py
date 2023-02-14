from django.shortcuts import render
from AppCafeReview.models import * 
from AppCafeReview.forms import *

# Create your views here.

def view_reviews(request): 
    allReviews = Cafeteria.objects.all()
    return render(request,"AppCafeReview/verReviews.html", {"allReviews": allReviews } )

def create_review(request): 
    if request.method == "POST":
 
            miFormulario = CafeteriaFormulario(request.POST)
            print(miFormulario)
 
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  cafeteria = Cafeteria(nombreCafeteria=informacion["nombreCafeteria"], 
                  puntajeCafeteria=informacion["puntajeCafeteria"],
                  puntajeServicio=informacion["puntajeServicio"],
                  puntajeAmbiente=informacion["puntajeAmbiente"],
                  fechaDeVisita=informacion["fechaDeVisita"],
                  comentario=informacion["comentario"], 
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
