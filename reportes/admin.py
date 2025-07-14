from django.contrib import admin
from .models import Reporte

@admin.register(Reporte) #registra una seccion en el panel del admin
class ReporteAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'id', 'usuario_comprador', 'usuario_vendedor', 'fecha', 'descripcion') #datos a mostrar
    list_filter = ('tipo', 'fecha') #el filtro de orden
    search_fields = ('descripcion', 'usuario_comprador__username', 'usuario_vendedor__username') #buscar por ...
    
    actions = ['marcar_como_resuelto', 'eliminar_reporte'] #acciones a tomar

    @admin.action(description='Marcar como resuelto (eliminar reporte)') #si se marca como resuelto ok
    def marcar_como_resuelto(self, request, queryset):
        queryset.delete()

    @admin.action(description='Eliminar reporte definitivamente') #si se marca como eliminado se borra de la lista (base de datos tambien)
    def eliminar_reporte(self, request, queryset):
        queryset.delete()

