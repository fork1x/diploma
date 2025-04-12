from django.urls import path
from main import views

app_name = 'main'  # Имя пространства имен для приложения main

urlpatterns = [  # Пути, которые относятся только к приложению main
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]