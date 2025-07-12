from django.urls import path
from . import views

urlpatterns = [
    path('', views.mis_chats, name='mis_chats'),
]