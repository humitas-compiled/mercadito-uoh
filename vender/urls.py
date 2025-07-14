from django.urls import path
from . import views

urlpatterns = [
    path('mis-productos/', views.mis_productos, name='mis_productos'),
    path('crear-producto/', views.crear_producto,name='crear_producto'),
    path('productos/editar/<int:producto_id>/', views.editar_producto, name='editar_producto'),
]