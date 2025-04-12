from django.shortcuts import render

def catalog(request):
    return render(request, 'goods/catalog.html') # https://mysite.com/catalog/

def product(request):
    return render(request, 'goods/product.html') # https://mysite.com/catalog/product/