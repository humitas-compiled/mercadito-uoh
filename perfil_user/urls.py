from django.urls import path
from . import views

urlpatterns = [
    path('mi-perfil/', views.ver_perfil, name='ver_perfil'),
    path('editar-perfil/', views.editar_perfil, name='editar_perfil')
]
