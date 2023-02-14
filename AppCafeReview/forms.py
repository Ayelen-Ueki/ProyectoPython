from django import forms 


class CafeteriaFormulario (forms.Form):
    nombreCafeteria = forms.CharField (max_length=30)
    puntajeCafeteria = forms.PositiveIntegerField()
    puntajeServicio = forms.PositiveIntegerField()
    puntajeAmbiente = forms.PositiveIntegerField()
    fechaDeVisita = forms.DateField()
    comentario = forms.CharField(max_length=200)
