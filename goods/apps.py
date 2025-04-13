# apps.py указывает некоторые настройки приложения
# в Django, такие как имя приложения и его отображаемое имя.

from django.apps import AppConfig


class GoodsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'goods'
    verbose_name = 'Товары'

