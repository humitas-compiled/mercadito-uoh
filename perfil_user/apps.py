from django.apps import AppConfig


class PerfilUserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'perfil_user'

    def ready(self):
        import perfil_user.signals