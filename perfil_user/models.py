from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    campus = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='perfiles/', blank=True, null=True)
    suspension = models.BooleanField(default=False)
    suspendido_hasta = models.DateTimeField(blank=True, null=True)

    def esta_suspendido(self):
        return self.suspendido_hasta and self.suspendido_hasta > timezone.now()

    def __str__(self):
        return self.user.username