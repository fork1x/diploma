from django.shortcuts import get_list_or_404, render, get_object_or_404
from goods.models import Products
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def catalog(request, category_slug, page=1):
    if category_slug == 'all':
        goods = Products.objects.all() # Получаем все товары из базы данных
    else:
        #goods = Products.objects.filter(category__slug=category_slug)
        goods = get_list_or_404(Products, category__slug=category_slug) # Получаем товары по категории

    paginator = Paginator(goods, 3) # Создаем пагинатор, который будет разбивать товары на страницы по 6 товаров на странице
    current_page = paginator.page(page) # Получаем текущую страницу

    context = {
        "title": "Каталог",
        "goods": current_page,
        "slug_url": category_slug}

    return render(request, 'goods/catalog.html', context) # https://mysite.com/catalog/

def product(request, product_slug):

    #product = get_object_or_404(Products.objects.filter(product_slug=product_slug)) # Получаем товар по id
    product = Products.objects.get(slug=product_slug) # Получаем товар по id

    context = {
        "product": product,
    }
    return render(request, 'goods/product.html', context=context) # https://mysite.com/catalog/product/


# Папка fixtures - это папка, в которой хранятся файлы с данными для заполнения базы данных.
# для заполнения базы данных используем команду: python3 manage.py loaddata fixtures/папка/название-файла.json