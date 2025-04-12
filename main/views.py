from django.http import HttpResponse
from django.shortcuts import render

def index(request) -> HttpResponse:
   context = {
       'title': 'Главная страница',
       'content': 'Магазин мебели HOME',
   }

   return render(request, 'main/index.html', context)

def about(request) -> HttpResponse:
    context = {
        'title': 'О нас',
        'content': 'О нас',
        'sample_text': 'Текст для проверки',
    }

    return render(request, 'main/about.html', context)