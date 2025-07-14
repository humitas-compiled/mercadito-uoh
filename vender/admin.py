from django.contrib import admin
from .models import Producto

# Configuracion para administrar productos desde el admin
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    # Columnas que se mostraran en la lista de productos
    list_display = ('nombre', 'usuario', 'publicado', 'categoria', 'campus', 'precio')
    list_filter = ('publicado', 'categoria', 'campus')
    search_fields = ('nombre', 'descripcion', 'usuario__username')

    actions = ['aceptar_publicacion', 'rechazar_publicacion'] #Acciones a realizar sobre los productos

    @admin.action(description='Aceptar publicación')
    def aceptar_publicacion(self, request, queryset): #Marca productos seleccionados como publicados
        queryset.update(publicado=True)

    @admin.action(description='Rechazar publicación (eliminar)')
    def rechazar_publicacion(self, request, queryset): #Elimina productos seleccionados
        queryset.delete()
