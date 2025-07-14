from django.contrib import admin
from .models import Perfil
from django.utils import timezone
from datetime import timedelta

@admin.register(Perfil)  #debe ser un admin 
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('user', 'email', 'telefono', 'campus', 'esta_suspendido') #lista a mostrar
    actions = ['suspender_3_dias', 'suspender_7_dias', 'quitar_suspension'] #acciones

    @admin.action(description='Suspender por 3 días') #cuando se escoge la suspensión por tres dias
    def suspender_3_dias(self, request, queryset):
        for perfil in queryset:
            perfil.suspendido_hasta = timezone.now() + timedelta(days=3)
            perfil.suspension = True
            perfil.save()

    @admin.action(description='Suspender por 7 días') #cuando se escoge la suspensión por siete dias
    def suspender_7_dias(self, request, queryset):
        for perfil in queryset:
            perfil.suspendido_hasta = timezone.now() + timedelta(days=7)
            perfil.suspension = True
            perfil.save()

    @admin.action(description='Quitar suspensión') #se quita la suspensión
    def quitar_suspension(self, request, queryset):
        queryset.update(suspendido_hasta=None, suspension = False)

    def esta_suspendido(self, obj): #si está suspendido
        return obj.esta_suspendido()
    esta_suspendido.boolean = True
    esta_suspendido.short_description = '¿Suspendido?'
