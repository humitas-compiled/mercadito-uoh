from django.shortcuts import render, redirect, get_object_or_404
from .models import Perfil
from .forms import PerfilForm
from django.contrib.auth.decorators import login_required

@login_required
def editar_perfil(request):
    perfil = get_object_or_404(Perfil, user=request.user)

    if request.method == "POST":
        form = PerfilForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('ver_perfil')  # o a donde quieras redirigir
    else:
        form = PerfilForm(instance=perfil)

    return render(request, 'editar_perfil/editar_perfil.html', {'form': form})

@login_required
def ver_perfil(request):
    try:
        perfil = Perfil.objects.get(user=request.user)
    except Perfil.DoesNotExist:
        perfil = None  # o redirige a crear perfil, etc.

    context = {
        'perfil': perfil
    }
    return render(request, 'ver_perfil/perfil.html', context)
