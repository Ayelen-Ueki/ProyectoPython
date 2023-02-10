from django.db import models

# Create your models here.

class Cafeteria (models.Model):
    nombreCafeteria = models.CharField (max_length=30)
    puntajeCafeteria = models.PositiveImageField()
    puntajeServicio = models.PositiveImageField()
    puntajeAmbiente = models.PositiveImageField()

class Reviewer (models.Model): 
    nombre = models.CharField (max_length=50)
    edad = models.PositiveImageField()
    fechaDeVisita = models.DateField()
    comentario = models.CharField(200)

class Owner (models.Model):
    nombre = models.CharField (max_length=50)
    nombreCafeteria = models.CharField (max_length=50)
    descripcion = models.CharField(200)


