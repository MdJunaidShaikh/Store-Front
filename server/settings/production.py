from .base import *
from server.settings import get_secret 

DEBUG = False

ALLOWED_HOSTS = ['*']

SECRET_KEY = get_secret('SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': get_secret('DB_NAME'),
        'USER': get_secret('DB_USER'),
        'PASSWORD': get_secret('DB_PASSWORD'),
        'HOST': get_secret('DB_HOST'),
        'PORT': get_secret('DB_PORT', '5432'),
    }
}
