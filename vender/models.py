from django.db import models
from django.contrib.auth.models import User

# Representa producto en venta
class Producto(models.Model):
    CATEGORIAS = [ #Opciones disponibles en categoria
        ('libros', 'Libros'),
        ('electrónica', 'Electrónica'),
        ('ropa', 'Ropa'),
        ('otros', 'Otros'),
    ]
    CAMPUS = [ #Opciones de campus
        ('rancagua', 'Campus Rancagua'),
        ('colchagua', 'Campus Colchagua'),
    ]

    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    campus = models.CharField(max_length=20, choices=CAMPUS)
    contacto = models.CharField(max_length=60)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    publicado = models.BooleanField(default=False)

    def __str__(self): 
        return self.nombre