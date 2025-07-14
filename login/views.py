from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required
from perfil_user.models import Perfil

# Vista para manejar el inicio de sesion
def login_view(request):
    if request.method == 'POST':
        # Obtiene el correo y la contraseña desde el formulario
        correo = request.POST['correo']
        password = request.POST['password']

        try:
            usuario = User.objects.get(email=correo) #Busca al usuario por su correo 

            if check_password(password, usuario.password): #Verifica la contraseña
                login(request, usuario) #Inicia sesion y redirige a pagina de compras   
                return redirect('compras')  #Vista que se muestra despues del login
            else:
                messages.error(request, "Contraseña incorrecta.") #Mensaje mostrado en caso de contraseña incorrecta
        except User.DoesNotExist:
            messages.error(request, "Correo no registrado.") #Correo no encontrado en la base de datos

    return render(request, 'login/login.html')

# Vista principal despues de iniciar sesion
@login_required
def inicio(request):
    if Perfil.suspension: #Verifica si el usuario esta suspendido
        raise Http404("Estás suspendido!")
    else: #Si no esta suspendido, muestra la pagina principal
        return render(request, 'compras/index.html')

# Vista para cerrar sesion
def logout_view(request):
    logout(request)
    return redirect('login')  #Termina sesion y redirige a la página de login