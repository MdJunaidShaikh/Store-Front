import os

DEBUG = True

ALLOWED_HOSTS = ['*']

SECRET_KEY = "8eQkzALyE0rYXvb+8sXUZkpjw7NfMVljCaVdWp2W"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
