from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required
from perfil_user.models import Perfil
# Create your views here.

def login_view(request):
    if request.method == 'POST':
        correo = request.POST['correo']
        password = request.POST['password']

        try:
            usuario = User.objects.get(email=correo)

            if check_password(password, usuario.password):
                login(request, usuario)
                return redirect('compras')  #funcion de vista dsp del login
            else:
                messages.error(request, "Contraseña incorrecta.")
        except User.DoesNotExist:
            messages.error(request, "Correo no registrado.")

    return render(request, 'login/login.html')

@login_required
def inicio(request):
    if Perfil.suspension:
        raise Http404("Estás suspendido!")
    else:
        return render(request, 'compras/index.html')

def logout_view(request):
    logout(request)
    return redirect('login')  #redirige a tu página de login