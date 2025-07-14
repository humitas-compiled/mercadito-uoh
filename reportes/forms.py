from django import forms
from .models import Reporte

class ReporteForm(forms.ModelForm): #los inputs para el form de reporte
    class Meta:
        model = Reporte
        fields = ['descripcion', 'tipo'] ##estos datos captan
