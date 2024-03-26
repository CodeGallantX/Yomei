"""
Django settings for BankApp project.

Generated by 'django-admin startproject' using Django 4.2.11.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
from django.core.mail import send_mail


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-y*cmw%kx##*hv-pv#pz2n@r-o)(#$=gkt$cg7j=6duc%syiv6b'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'InfinityFinance',
    'material',
    'material.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'BankApp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["templates"],
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

WSGI_APPLICATION = 'BankApp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Admin Details and SMTP
ADMIN_EMAIL = 'sayojami2007@gmail.com'

# SMTP
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.example.com'  # Replace with your SMTP server
EMAIL_PORT = 587  # Replace with your SMTP port
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'sayojami2007@gmail.com'  # Replace with your email address
EMAIL_HOST_PASSWORD = 'your_password'


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

'''
# Optionally, you can add configuration settings for Django Material Admin
MATERIAL_ADMIN_SITE = {
    # Specify a custom site header
    'HEADER': 'STAFF ADMINISTRATION',

    # Optionally, specify a custom site title
    'SITE_TITLE': 'STAFF ADMINISTRATION',

    # Optionally, specify a custom site footer
    'SITE_FOOTER': 'Your Site Footer',
    
    # Specify the menu structure for the sidebar
    'MENU': (
        # Example menu items
        {'label': 'Dashboard', 'icon': 'dashboard', 'url': '/admin/', 'permissions': ['auth.view_user']},
        {'label': 'Users', 'icon': 'group', 'models': ('auth.user', 'auth.group')},
        {'label': 'Content', 'icon': 'content_paste', 'app_list': (
            {'app_label': 'app1', 'models': ('app1.model1', 'app1.model2')},
            {'app_label': 'app2', 'models': ('app2.model1', 'app2.model2')},
        )},
    ),
    
    # Optionally, specify a custom theme
    'OPTIONS': {
        'HEADER': '#3F51B5',
        'COLOR': '#00040f',
        'COLLAPSED_COLOR': '#FF9800',
        'PAGINATOR_COLOR': '#ffd700',
        'HEADER_TITLE_COLOR': 'white',
        'DISABLE_PANEL_COLLAPSE': False,
        'BREADCRUMB': True,
        'BREADCRUMB_LINK': True,
        'SET_FIXED_DRAWER': False,
        'SET_MINI_DRAWER': False,
        'SET_DRAWER': True,
        'SET_HEADER': True,
        'SET_NAV_ICON': True,
    },
}
'''