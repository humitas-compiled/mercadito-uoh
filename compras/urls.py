from django.urls import path
from . import views

# Lista urls para funcionalida seccion compras
urlpatterns = [
    path('', views.seccion_compras, name="compras"),
    path('ver-producto/<int:id>/', views.ver_producto, name='ver_producto'),
    path('iniciar/<int:producto_id>/', views.iniciar_chat, name='iniciar_chat'),
]