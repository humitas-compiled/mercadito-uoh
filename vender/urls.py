from django.urls import path
from . import views

urlpatterns = [
    path('mis-productos/', views.mis_productos, name='mis_productos'),
    path('crear/', views.crear_producto,name='crear_producto'),
]