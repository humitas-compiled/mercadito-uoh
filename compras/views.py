from vender.models import Producto
from chat.models import Chat
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Vista de la seccion de compras, muestra los productos publicados 
@login_required
def seccion_compras(request):
    query = request.GET.get('q')
    if query:
        # Si se busca, filtra por nombre
        productos = Producto.objects.filter(
            Q(nombre__icontains=query) | Q(descripcion__icontains=query),
            publicado=True
        ).exclude(usuario=request.user) #No muestra los productos del usuario
    else:
        productos = Producto.objects.filter(publicado=True).exclude(usuario=request.user)
    
    # Renderiza la pagina con los productos que cumplen la busqueda
    return render(request, 'compras/index.html', {'productos': productos})

# Vista para ver los detalles de un producto especifico 
def ver_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'ver-producto/ver_producto.html', {'producto': producto})

# Vista para iniciar un chat con el vendedor del producto
@login_required
def iniciar_chat(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    
    vendedor = producto.usuario  # El usuario que creó el producto

    # Verifica si ya existe un chat con ese comprador y el producto
    chat = Chat.objects.filter(producto=producto, comprador=request.user).first()
    if chat:
        # Si ya existe, lo redirige
        return redirect('mis_chats', chat_id=chat.id)

    # Si no existe, crea un nuevo chat
    chat = Chat.objects.create(
        producto=producto,
        comprador=request.user,
        vendedor=vendedor
    )
    return redirect('mis_chats', chat_id=chat.id) #Redirige al chat recien creado
