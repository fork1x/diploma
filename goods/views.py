from django.shortcuts import get_list_or_404, render, get_object_or_404
from goods.models import Products
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from goods.utils import q_search


def catalog(request, category_slug=None):

    page = request.GET.get('page', 1) # Получаем номер страницы из GET-запроса. Если номер страницы не указан, то по умолчанию будет 1
    on_sale = request.GET.get('on_sale', None) # Получаем параметр on_sale из GET-запроса. Если параметр не указан, то по умолчанию будет None
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', None)

    if category_slug == 'all':
        goods = Products.objects.all() # Получаем все товары из базы данных
    
    elif query:
        goods = q_search(query)
    
    else:
        #goods = Products.objects.filter(category__slug=category_slug)
        goods = get_list_or_404(Products, category__slug=category_slug) # Получаем товары по категории


    if on_sale:
        goods = goods.filter(discount__gt=0) # Если параметр on_sale указан, то фильтруем товары по скидке

    if order_by and order_by != 'default':
        goods = goods.order_by(order_by) # Если параметр order_by указан, то сортируем товары по указанному параметру



    paginator = Paginator(goods, 3) # Создаем пагинатор, который будет разбивать товары на страницы по 6 товаров на странице
    current_page = paginator.page(round(int(page))) # Получаем текущую страницу

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