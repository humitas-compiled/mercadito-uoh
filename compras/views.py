from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def seccion_compras(request):
    return render(request, 'compras/index.html')