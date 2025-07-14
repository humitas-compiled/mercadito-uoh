from django.shortcuts import render, get_object_or_404, redirect
from .models import Chat, Mensaje
from django.contrib.auth.decorators import login_required
from django.db.models import Q

@login_required
def mis_chats(request, chat_id=None):
    # Obtiene todos los chats donde el usuario es comprador o vendedor
    chats = Chat.objects.filter(Q(comprador=request.user) | Q(vendedor=request.user)).distinct().order_by('-creado_en')

    chat_seleccionado = None
    if chat_id:
        chat_seleccionado = get_object_or_404(chats, id=chat_id)
        if chat_seleccionado:
            if chat_seleccionado.comprador != request.user:
                otro_usuario = chat_seleccionado.comprador
            else:
                otro_usuario = chat_seleccionado.vendedor
        # Si se envió un mensaje
        if request.method == 'POST':
            contenido = request.POST.get('contenido', '').strip()
            if contenido:
                Mensaje.objects.create(chat=chat_seleccionado, autor=request.user, contenido=contenido)
                return redirect('mis_chats', chat_id=chat_id)  # Evita reenvío

    return render(request, 'main/chats.html', {
        'chats': chats,
        'chat_seleccionado': chat_seleccionado,
        'otro_usuario': otro_usuario if chat_seleccionado else None
    })

@login_required
def enviar_mensaje(request, chat_id):
    if request.method == 'POST':
        chat = get_object_or_404(Chat, id=chat_id)
        contenido = request.POST.get('contenido')
        if contenido:
            Mensaje.objects.create(chat=chat, autor=request.user, contenido=contenido)
        return redirect('mis_chats', chat_id=chat.id)
    else:
        return redirect('mis_chats')

"""def mis_chats(request):
    return render(request, 'main/chats.html')"""