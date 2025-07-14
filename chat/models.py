from django.db import models
from django.contrib.auth.models import User
from vender.models import Producto

# Modelo que representa un chat entre comprador y vendedor relacionado a un producto
class Chat(models.Model):
    # Producto sobre el cual se abre el chat
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    # Usuario comprador
    comprador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chats_comprados')
    # Usuario vendedor
    vendedor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chats_vendidos')
    # Fecha y hora de creacion 
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Chat sobre {self.producto.nombre} - {self.comprador.username}"

# Modelo que representa mensaje en el chat
class Mensaje(models.Model):
    # Chat al que pertenece el mensaje
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='mensajes')
    # Usuario que envia el mensaje
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    # Contenido mensaje
    contenido = models.TextField()
    # Fecha y hora mensaje
    enviado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.autor.username}: {self.contenido[:20]}"