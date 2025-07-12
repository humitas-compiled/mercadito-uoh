from django.urls import path
from . import views

urlpatterns = [
    path('', views.seccion_compras, name="compras"),
    path("producto/", views.ver_producto, name="producto")
]