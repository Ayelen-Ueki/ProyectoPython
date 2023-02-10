from django.db import models

# Create your models here.

class Cafeteria (models.Model):
    nombreCafeteria = models.CharField (max_length=30)
    puntajeCafeteria = models.PositiveIntegerField()
    puntajeServicio = models.PositiveIntegerField()
    puntajeAmbiente = models.PositiveIntegerField()

class Reviewer (models.Model): 
    nombre = models.CharField (max_length=50)
    edad = models.PositiveIntegerField()
    fechaDeVisita = models.DateField()
    comentario = models.CharField(max_length=200)

class Owner (models.Model):
    nombre = models.CharField (max_length=50)
    nombreCafeteria = models.CharField (max_length=50)
    descripcion = models.CharField(max_length=200)


