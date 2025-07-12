from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import ProductoForm
from .models import Producto


# Create your views here.
@login_required
def mis_productos(request):
    productos = Producto.objects.all()
    return render(request, 'vender/mis_productos.html', {'productos': productos})

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.usuario = request.user  # Asigna el usuario actual
            producto.save()
            return redirect('mis_productos')  # ajusta según tu ruta
    else:
        form = ProductoForm()
    
    return render(request, 'crear/crear_producto.html', {'form': form})