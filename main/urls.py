from django.urls import path
from main import views

app_name = 'main'  # Имя пространства имен для приложения main

urlpatterns = [  # Пути, которые относятся только к приложению main
    path('', views.index, name='index'), # Путь на главную страницу. Пусто означает, что это корень сайта. https://mysite.com/
    # Эта строка определяет маршрут для корня внутри приложения main. То есть, если запрос передан из глобального urls.py (app) в urls.py (main),
    # и путь совпадает с '' (корень), то будет вызвана функция views.index.
    path('about/', views.about, name='about'), # https://mysite.com/about/
]