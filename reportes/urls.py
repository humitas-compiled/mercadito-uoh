from django.urls import path
from . import views

urlpatterns = [
    path('<str:tipo>/<int:objeto_id>/', views.reportar, name='reportar'),
]