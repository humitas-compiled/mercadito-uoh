from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required
# Create your views here.

def login_view(request):
    if request.method == 'POST':
        correo = request.POST['correo']
        password = request.POST['password']

        try:
            usuario = User.objects.get(email=correo)

            if check_password(password, usuario.password):
                login(request, usuario)
                return redirect('seccion_compras')  #funcion de vista dsp del login
            else:
                messages.error(request, "Contraseña incorrecta.")
        except User.DoesNotExist:
            messages.error(request, "Correo no registrado.")

    return render(request, 'login/login.html')

@login_required
def inicio(request):
    return render(request, 'compras/index.html')  # o el template que tú quieras

def logout_view(request):
    logout(request)
    return redirect('login')  # redirige a tu página de login

def hola(request):
    return HttpResponse("hola")