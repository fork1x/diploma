from django.urls import path
from users import views

app_name = 'users'  # Имя пространства имен для приложения users

urlpatterns = [  # Пути, которые относятся только к приложению users
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
]