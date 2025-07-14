from django.db.models.signals import post_save #señal q se envia después de guardar datos en la bd
from django.dispatch import receiver
from django.contrib.auth.models import User #el User es el modelo por defecto de django
from .models import Perfil #nuestro modelo personalizado de User

@receiver(post_save, sender=User)
def crear_perfil_usuario(sender, instance, created):
    if created:
        Perfil.objects.create(user=instance) #si un user es creado, se crea un perfil (instancia) asociado a ese User.
