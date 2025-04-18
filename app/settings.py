from pathlib import Path
from dotenv import load_dotenv
import os
import dj_database_url

load_dotenv('.env')

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = os.environ.get('DEBUG') == 'True'

ALLOWED_HOSTS = [os.environ.get('ALLOWED_HOSTS', '*')]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',  # Статические файлы
    'django.contrib.postgres',  # PostgreSQL

    'debug_toolbar',  # Отладка

    'main', # Основное приложение
    'goods', # Приложение для товаров
    'users', # Приложение для пользователей
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    "debug_toolbar.middleware.DebugToolbarMiddleware", # Отладка
    "whitenoise.middleware.WhiteNoiseMiddleware", # Для работы с статическими файлами на Heroku
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Папка для хранения шаблонов
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'



DATABASES = {}

if DEBUG:
        DATABASES['default'] = {

            'ENGINE': 'django.db.backends.postgresql', # Используем PostgreSQL
            'NAME': 'home',
            'USER': 'home',
            'PASSWORD': 'home',
            'HOST': 'localhost',
            'PORT': '5432',
    }
else:
    DATABASES['default'] = dj_database_url.config(
        default=os.environ.get('DATABASE_URL'),
        conn_max_age=600,
        conn_health_checks=True
    )


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]





LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images) and media files

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Папка для хранения статических файлов
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]  # Папка для хранения статических файлов в приложении


MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'  # Папка для хранения загруженных файлов





DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.User'  # Модель пользователя


INTERNAL_IPS = [ # для отладки
    # ...
    "127.0.0.1",
    # ...
]

LOGIN_URL = '/user/login'  # URL для перенаправления при неавторизованном доступе