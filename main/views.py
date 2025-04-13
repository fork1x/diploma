from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories

def index(request) -> HttpResponse:
   
   categories = Categories.objects.all()
   context = {
       'title': 'Главная страница',
       'content': 'Магазин мебели HOME',
       'categories': categories,
   }

   return render(request, 'main/index.html', context)

def about(request) -> HttpResponse:
    context = {
        'title': 'О нас',
        'content': 'О нас',
        'sample_text': 'Текст для проверки',
    }

    return render(request, 'main/about.html', context)