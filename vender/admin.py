from django.contrib import admin
from .models import Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'usuario', 'publicado', 'categoria', 'campus', 'precio')
    list_filter = ('publicado', 'categoria', 'campus')
    search_fields = ('nombre', 'descripcion', 'usuario__username')

    actions = ['aceptar_publicacion', 'rechazar_publicacion']

    @admin.action(description='Aceptar publicación')
    def aceptar_publicacion(self, request, queryset):
        queryset.update(publicado=True)

    @admin.action(description='Rechazar publicación (eliminar)')
    def rechazar_publicacion(self, request, queryset):
        queryset.delete()
