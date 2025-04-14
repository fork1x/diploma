from django.shortcuts import render

from goods.models import Products


def catalog(request):
    goods = Products.objects.all() # Получаем все товары из базы данных

    context = {
   "title": "Каталог",
   "goods": goods,
    }

    return render(request, 'goods/catalog.html', context) # https://mysite.com/catalog/

def product(request):
    return render(request, 'goods/product.html') # https://mysite.com/catalog/product/


# Папка fixtures - это папка, в которой хранятся файлы с данными для заполнения базы данных.
# для заполнения базы данных используем команду: python3 manage.py loaddata fixtures/папка/название-файла.json
