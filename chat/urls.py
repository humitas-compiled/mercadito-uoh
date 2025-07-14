from django.urls import path
from . import views

urlpatterns = [
    path('', views.mis_chats, name='mis_chats'),
    path('<int:chat_id>/', views.mis_chats, name='mis_chats'),
    path('chats/enviar/<int:chat_id>/', views.enviar_mensaje, name='enviar_mensaje'),
]
