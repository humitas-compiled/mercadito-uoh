from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    campus = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='perfiles/', blank=True, null=True)

    def __str__(self):
        return f'Perfil de {self.user.username}'