from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import ProductoForm


# Create your views here.
@login_required
def mis_productos(request):
    return render(request, 'vender/mis_productos.html')

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mis_productos')  # ajusta según tu ruta
    else:
        form = ProductoForm()
    
    return render(request, 'crear/crear_producto.html', {'form': form})