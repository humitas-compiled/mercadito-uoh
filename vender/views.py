from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def mis_productos(request):
    return render(request, 'vender/mis_productos.html')

def crear_producto(request):
    return render(request, 'crear/crearproducto.html')