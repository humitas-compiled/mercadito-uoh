from django import forms
from .models import Perfil

#formulario para captar los los campos que explicitan del usuario
class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['telefono', 'email', 'campus', 'imagen']