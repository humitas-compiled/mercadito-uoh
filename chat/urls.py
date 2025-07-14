from django.urls import path
from . import views

# Lista de urls para funcionalidad de chats 
urlpatterns = [
    path('', views.mis_chats, name='mis_chats'), #Pagina principal
    path('<int:chat_id>/', views.mis_chats, name='mis_chats'), #Chat especifico
    path('chats/enviar/<int:chat_id>/', views.enviar_mensaje, name='enviar_mensaje'), #Enviar mensaje a chat especifico
]
