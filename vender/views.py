from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ProductoForm
from .models import Producto


# Create your views here.
@login_required
def mis_productos(request):
    productos = Producto.objects.filter(usuario=request.user, publicado=True)
    return render(request, 'vender/mis_productos.html', {'productos': productos})

@login_required
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

@login_required
def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id, usuario=request.user)

    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('mis_productos')  # Ajusta si tu vista se llama distinto
    else:
        form = ProductoForm(instance=producto)

    return render(request, 'crear/crear_producto.html', {'form': form, 'producto': producto})