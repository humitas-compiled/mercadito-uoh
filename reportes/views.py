from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from vender.models import Producto
from chat.models import Chat
from .models import Reporte
from .forms import ReporteForm

@login_required
def reportar(request, tipo, objeto_id):
    if tipo == 'producto':
        objeto = get_object_or_404(Producto, id=objeto_id)
        usuario_vendedor = objeto.usuario
        nombre = objeto.nombre
    elif tipo == 'chat':
        objeto = get_object_or_404(Chat, id=objeto_id)
        usuario_vendedor = objeto.vendedor if objeto.comprador == request.user else objeto.comprador
        nombre = f'Chat con {usuario_vendedor.username}'
    else:
        return HttpResponseRedirect('/compras/')  # redirige a algún lugar si el tipo no es válido

    if request.method == 'POST':
        form = ReporteForm(request.POST)
        if form.is_valid():
            reporte = form.save(commit=False)
            reporte.usuario_comprador = request.user
            reporte.usuario_vendedor = usuario_vendedor
            reporte.nombre = nombre
            reporte.tipo = tipo
            reporte.save()
            return HttpResponseRedirect('/compras/')  # o donde necesites
    else:
        form = ReporteForm()

    context = {
        'form': form,
        'tipo': tipo,
        'nombre': nombre,
    }

    return render(request, 'reportes/temp_reportes.html', context)
