from django.db import models
from django.contrib.auth.models import User

class Reporte(models.Model):
    TIPO_CHOICES = [
        ('producto', 'Producto'),
        ('chat', 'Chat'), #para la combo box
    ]

    usuario_comprador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reportes_realizados')
    usuario_vendedor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reportes_recibidos')
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    fecha = models.DateTimeField(auto_now_add=True)

    #datos que van en la base de datos y la lista que verá el admin (algunos datos)

    def __str__(self):
        return f"{self.tipo.title()} - {self.nombre}"