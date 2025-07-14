from django.db import models
from django.contrib.auth.models import User
from vender.models import Producto

class Chat(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    comprador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chats_comprados')
    vendedor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chats_vendidos')
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Chat sobre {self.producto.nombre} - {self.comprador.username}"

class Mensaje(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='mensajes')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()
    enviado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.autor.username}: {self.contenido[:20]}"