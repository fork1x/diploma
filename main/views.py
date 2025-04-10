from django.http import HttpResponse
from django.shortcuts import render

def index(request) -> HttpResponse:
    context = {
        'title': 'Hello World',
        'content': 'Welcome to the Django app!',
    }

    return render(request, 'main/index.html', context)

def about(request) -> HttpResponse:
    return HttpResponse('About page')