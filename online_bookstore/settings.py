import os

from pathlib import Path
<<<<<<< HEAD
 
=======

>>>>>>> f2382b6baa6435a311c316d541563b2245312faf
# Base directory

BASE_DIR = Path(__file__).resolve().parent.parent
 
# SECURITY WARNING: keep the secret key used in production secret!

<<<<<<< HEAD
SECRET_KEY = 'django-insecure-change-this-in-production'
 
# DEVELOPMENT MODE ONLY

DEBUG = True
 
# ⚠️ Allow all hosts for development

ALLOWED_HOSTS = ['*']
 
# Application definition

=======
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-change-this-in-production'

# DEVELOPMENT MODE ONLY
DEBUG = True

# ⚠️ Allow all hosts for development
ALLOWED_HOSTS = ['*']

# Application definition
>>>>>>> f2382b6baa6435a311c316d541563b2245312faf
INSTALLED_APPS = [

    'django.contrib.admin',

    'django.contrib.auth',

    'django.contrib.contenttypes',

    'django.contrib.sessions',

    'django.contrib.messages',

    'django.contrib.staticfiles',
<<<<<<< HEAD

    'books',  # your app

]
 
=======
    'books',  # your app
]

>>>>>>> f2382b6baa6435a311c316d541563b2245312faf
MIDDLEWARE = [

    'django.middleware.security.SecurityMiddleware',
<<<<<<< HEAD

=======
>>>>>>> f2382b6baa6435a311c316d541563b2245312faf
    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.common.CommonMiddleware',

    'django.middleware.csrf.CsrfViewMiddleware',

    'django.contrib.auth.middleware.AuthenticationMiddleware',

    'django.contrib.messages.middleware.MessageMiddleware',

    'django.middleware.clickjacking.XFrameOptionsMiddleware',

<<<<<<< HEAD
]
 
ROOT_URLCONF = 'online_bookstore.urls'
 
=======
ROOT_URLCONF = 'online_bookstore.urls'

>>>>>>> f2382b6baa6435a311c316d541563b2245312faf
TEMPLATES = [

    {

        'BACKEND': 'django.template.backends.django.DjangoTemplates',
<<<<<<< HEAD

        'DIRS': [BASE_DIR / 'templates'],  # optional: custom template directory

=======
        'DIRS': [BASE_DIR / 'templates'],  # optional: custom template directory
>>>>>>> f2382b6baa6435a311c316d541563b2245312faf
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

<<<<<<< HEAD
]
 
=======
>>>>>>> f2382b6baa6435a311c316d541563b2245312faf
WSGI_APPLICATION = 'online_bookstore.wsgi.application'
 
# Database: SQLite for development

DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.sqlite3',

        'NAME': BASE_DIR / 'db.sqlite3',

<<<<<<< HEAD
=======
# Database: SQLite for development
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
>>>>>>> f2382b6baa6435a311c316d541563b2245312faf
    }
}

}
 
# Password validation

AUTH_PASSWORD_VALIDATORS = [
<<<<<<< HEAD

    {

        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',

    },

    {

        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',

    },

=======
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
>>>>>>> f2382b6baa6435a311c316d541563b2245312faf
]
 
# Internationalization

<<<<<<< HEAD
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

=======
# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
>>>>>>> f2382b6baa6435a311c316d541563b2245312faf
USE_I18N = True

USE_TZ = True
 
# Static files
<<<<<<< HEAD

STATIC_URL = '/static/'

STATICFILES_DIRS = [BASE_DIR / 'static']  # optional

STATIC_ROOT = BASE_DIR / 'staticfiles'
 
# Default primary key field type

=======
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']  # optional
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Default primary key field type
>>>>>>> f2382b6baa6435a311c316d541563b2245312faf
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

 