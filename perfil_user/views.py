from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Perfil
from .forms import PerfilForm
from django.contrib.auth.decorators import login_required


#todos los que tienen el decorador necesitan un user autenticado

#creamos la vista editar perfil que necesita el usuario actual y nos lleva a el template editar_perfil
@login_required
def editar_perfil(request):
    perfil = get_object_or_404(Perfil, user=request.user)

    if request.method == "POST":
        form = PerfilForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('ver_perfil') #cuando se completa me redirija a la vista de mi perfil
    else:
        form = PerfilForm(instance=perfil)

    return render(request, 'editar_perfil/editar_perfil.html', {'form': form})

#esta es la vista de mi perfil
@login_required
def ver_perfil(request):
    try:
        perfil = Perfil.objects.get(user=request.user)
    except Perfil.DoesNotExist:
        perfil = None  

    context = {
        'perfil': perfil #esto se pasará al template pra mostrar la info
    }
    return render(request, 'ver_perfil/perfil.html', context)

@login_required
def ver_perfil_otro(request, user_id):
    usuario = get_object_or_404(User, id=user_id) #busca un obj user donde el id sea igual a user_id sino tira error 404
    perfil = get_object_or_404(Perfil, user=usuario) #acá vincula el perfil al usuario

    context = {
        'usuario': usuario,
        'perfil': perfil, #datos para el template
    }
    return render(request, 'ver_perfil/perfil_otro.html', context) 
