from django import forms 


class CafeteriaFormulario (forms.Form):
    nombreCafeteria = forms.CharField (max_length=30)
    puntajeCafeteria = forms.IntegerField()
    puntajeServicio = forms.IntegerField()
    puntajeAmbiente = forms.IntegerField()
    fechaDeVisita = forms.DateField()
    comentario = forms.CharField(max_length=200)
    
class EditarFormulario (forms.Form):
    nombreCafeteria = forms.CharField (max_length=30)
    puntajeCafeteria = forms.IntegerField()
    puntajeServicio = forms.IntegerField()
    puntajeAmbiente = forms.IntegerField()
    fechaDeVisita = forms.DateField()
    comentario = forms.CharField(max_length=200)
    
