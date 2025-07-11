from django.db import models

class Producto(models.Model):
    CATEGORIAS = [
        ('libros', 'Libros'),
        ('electronica', 'Electrónica'),
        ('ropa', 'Ropa'),
        ('otros', 'Otros'),
    ]
    CAMPUS = [
        ('rancagua', 'Campus Rancagua'),
        ('colchagua', 'Campus Colchagua'),
    ]

    name = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    campus = models.CharField(max_length=20, choices=CAMPUS)
    contacto = models.CharField(max_length=60)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)

    def __str__(self):
        return self.name