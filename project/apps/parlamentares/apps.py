from django.apps import AppConfig


class ParlamentaresConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'parlamentares'
    def ready(self):
        from . import menu