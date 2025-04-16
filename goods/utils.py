from goods.models import Products
from django.db.models import Q # Импортируем класс Q из модуля django.db.models для создания сложных запросов к базе данных

def q_search(query):
    if query.isdigit() and len(query) <= 3:
        return Products.objects.filter(id=int(query))
    
    keywords = [word for word in query.split() if len(word) > 2] # Разбиваем строку на слова и оставляем только те, которые длиннее 2 символов

    q_objects = Q() # Создаем объект Q для создания сложных запросов к базе данных

    for token in keywords:
        q_objects |= Q(description__icontains=token) # Добавляем условие поиска по описанию товара
        q_objects |= Q(name__icontains=token)

    return Products.objects.filter(q_objects) # Возвращаем товары, которые соответствуют условиям поиска