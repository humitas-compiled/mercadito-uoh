from django.shortcuts import render, get_object_or_404, redirect
from .models import Chat, Mensaje
from django.contrib.auth.decorators import login_required
from django.db.models import Q

@login_required
def mis_chats(request, chat_id=None):
    # Obtiene todos los chats donde el usuario es comprador o vendedor
    chats = Chat.objects.filter(Q(comprador=request.user) | Q(vendedor=request.user)).distinct().order_by('-creado_en')

    chat_seleccionado = None #Inicia el chat seleccionado
    if chat_id:
        # Obtiene el chat seleccionado o muestra error si no existe
        chat_seleccionado = get_object_or_404(chats, id=chat_id)
        if chat_seleccionado:
            # Identifica al otro usuario que participa en el chat
            if chat_seleccionado.comprador != request.user:
                otro_usuario = chat_seleccionado.comprador
            else:
                otro_usuario = chat_seleccionado.vendedor
        # Si se envia un mensaje 
        if request.method == 'POST':
            contenido = request.POST.get('contenido', '').strip()
            if contenido:
                # Crea mensaje y lo guarda
                Mensaje.objects.create(chat=chat_seleccionado, autor=request.user, contenido=contenido)
                # Redirige para evitar que el mensaje se envie dos veces
                return redirect('mis_chats', chat_id=chat_id) 

    # Renderiza la lista de chats y el chat seleccionado
    return render(request, 'main/chats.html', {
        'chats': chats,
        'chat_seleccionado': chat_seleccionado,
        'otro_usuario': otro_usuario if chat_seleccionado else None
    })

@login_required
def enviar_mensaje(request, chat_id):
    # Obtiene el chat seleccionado o muestra error si no existe
    if request.method == 'POST':
        chat = get_object_or_404(Chat, id=chat_id)
        contenido = request.POST.get('contenido')
        if contenido:
            # Crea el mensaje 
            Mensaje.objects.create(chat=chat, autor=request.user, contenido=contenido)
        # Redirige a la vista de mis_chats para mostrar los mensajes actualizados 
        return redirect('mis_chats', chat_id=chat.id)
    else:
        return redirect('mis_chats')

