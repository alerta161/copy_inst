from django.apps import AppConfig


class MywebMainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myweb_main'

    def ready(self):
        from . import signals
        super().ready()