from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

def seccion_compras(request):
    return render(request, 'compras/index.html')

"""@login_required
def mis_productos(request):
    return render(request, 'vender/templates/vender/mis_productos.html')  # asegúrate de tener esta plantilla"""

def ver_producto(request):
    return render(request, 'ver-producto/ver_producto.html')