from vender.models import Producto
from chat.models import Chat
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# Create your views here.

@login_required
def seccion_compras(request):
    query = request.GET.get('q')
    if query:
        productos = Producto.objects.filter(
            Q(nombre__icontains=query) | Q(descripcion__icontains=query),
            publicado=True
        ).exclude(usuario=request.user)
    else:
        productos = Producto.objects.filter(publicado=True).exclude(usuario=request.user)
    
    return render(request, 'compras/index.html', {'productos': productos})

def ver_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'ver-producto/ver_producto.html', {'producto': producto})

@login_required
def iniciar_chat(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    
    vendedor = producto.usuario  # El usuario que creó el producto

    # Verifica si ya existe un chat para ese producto y comprador
    chat = Chat.objects.filter(producto=producto, comprador=request.user).first()
    if chat:
        return redirect('mis_chats', chat_id=chat.id)

    # Crear un nuevo chat, asignando vendedor y comprador
    chat = Chat.objects.create(
        producto=producto,
        comprador=request.user,
        vendedor=vendedor
    )
    return redirect('mis_chats', chat_id=chat.id)
