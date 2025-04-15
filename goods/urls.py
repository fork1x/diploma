from django.urls import path
from goods import views

app_name = 'goods'  # Имя пространства имен для приложения goods

urlpatterns = [  # Пути, которые относятся только к приложению goods
    path('<slug:category_slug>/', views.catalog, name='index'), # Путь на главную страницу. Пусто означает, что это корень сайта. https://mysite.com/
    path('<slug:category_slug>/<int:page>', views.catalog, name='index'),
    path('product/<slug:product_slug>/', views.product, name='product'),
]