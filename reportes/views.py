from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from vender.models import Producto
from chat.models import Chat
from .forms import ReporteForm

@login_required #se requiere autenticación
def reportar(request, tipo, objeto_id):
    if tipo == 'producto': #aquí definimos el tipo de reporte y quien será el/la reportad@ de cada sección (vendedor/otra persona del chat)
        objeto = get_object_or_404(Producto, id=objeto_id)
        usuario_vendedor = objeto.usuario
        nombre = objeto.nombre
    elif tipo == 'chat':
        objeto = get_object_or_404(Chat, id=objeto_id)
        usuario_vendedor = objeto.vendedor if objeto.comprador == request.user else objeto.comprador 
        nombre = f'Chat con {usuario_vendedor.username}'
    else:
        return HttpResponseRedirect('/compras/')  #lleva a la seccion compras

    if request.method == 'POST': #datos para el formulario
        form = ReporteForm(request.POST)
        if form.is_valid(): 
            reporte = form.save(commit=False) #si es valido se crea un objeto reporte sin guardar aún
            reporte.usuario_comprador = request.user
            reporte.usuario_vendedor = usuario_vendedor 
            reporte.nombre = nombre
            reporte.tipo = tipo
            reporte.save() #se guarda en la bd
            return HttpResponseRedirect('/compras/')  
    else:
        form = ReporteForm()

    context = {
        'form': form,
        'tipo': tipo,
        'nombre': nombre, #datos para el template
    }

    return render(request, 'reportes/temp_reportes.html', context)
