# tags.py хранит пользовательские теги и фильтры
from django.utils.http import urlencode
from django import template # импортируем модуль template для создания тегов
from goods.models import Categories # импортируем модель Category из приложения goods

register = template.Library() # создаем экземпляр библиотеки тегов

@register.simple_tag # регистрируем тег который служит для получения всех категорий на всех страницах
def categories():
    # Получаем все категории из базы данных
    return Categories.objects.all()

@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)