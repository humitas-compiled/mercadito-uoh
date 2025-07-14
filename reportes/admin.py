from django.contrib import admin
from .models import Reporte

@admin.register(Reporte)
class ReporteAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'id', 'usuario_comprador', 'usuario_vendedor', 'fecha', 'descripcion')
    list_filter = ('tipo', 'fecha')
    search_fields = ('descripcion', 'usuario_comprador__username', 'usuario_vendedor__username')
    
    actions = ['marcar_como_resuelto', 'eliminar_reporte']

    @admin.action(description='Marcar como resuelto (eliminar reporte)')
    def marcar_como_resuelto(self, request, queryset):
        queryset.delete()

    @admin.action(description='Eliminar reporte definitivamente')
    def eliminar_reporte(self, request, queryset):
        queryset.delete()

