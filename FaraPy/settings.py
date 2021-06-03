"""
Django settings for FaraPy project.

Generated by 'django-admin startproject' using Django 2.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=fz)7she4ka9-2-v2_+nu0ofl5f+msll*d1vcqys+!c@8ftqug'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = '/'
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'blog',
    'django_jalali',
    'jdatetime',
    'ckeditor_uploader',
    'ckeditor',
    'sorl.thumbnail',
    'widget_tweaks',
    'kavenegar',
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

ROOT_URLCONF = 'FaraPy.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),os.path.join(BASE_DIR, 'themes')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'blog.context_processors.context',
            ],
        },
    },
]
LOGIN_URL = 'blog.views.login_user'

WSGI_APPLICATION = 'FaraPy.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'data/db.sqlite3'),
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'sharp_euclid',
#         'USER': 'root',
#         'PASSWORD': 'WDbBbn2v3XrIO7qyclCd0uiR',
#         'HOST': 's10.liara.ir',   # Or an IP Address that your DB is hosted on
#         'PORT': '32232',
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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

JALALI_DATE_DEFAULTS = {
   'Strftime': {
        'date': '%y/%m/%d',
        'datetime': '%H:%M:%S _ %y/%m/%d',
    },
    'Static': {
        'js': [
            # loading default jQuery
            'admin/jquery.ui.datepicker.jalali/scripts/jquery-1.10.2.min.js',
            # loading datepicker
            'admin/js/django_jalali.min.js',
            # OR
            # 'admin/jquery.ui.datepicker.jalali/scripts/jquery-1.10.2.min.js',
            # 'admin/jquery.ui.datepicker.jalali/scripts/jquery.ui.core.js',
            # 'admin/jquery.ui.datepicker.jalali/scripts/calendar.js',
            # 'admin/jquery.ui.datepicker.jalali/scripts/jquery.ui.datepicker-cc.js',
            # 'admin/jquery.ui.datepicker.jalali/scripts/jquery.ui.datepicker-cc-fa.js',
            # 'admin/js/main.js',
        ],
        'css': {
            'all': [
                'admin/jquery.ui.datepicker.jalali/themes/base/jquery-ui.min.css',
            ]
        }
    },
}






# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/
CKEDITOR_UPLOAD_PATH = "uploads/"

LANGUAGE_CODE = 'en-uk'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
Themes_Root =  os.path.join(BASE_DIR, 'themes')
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
Themes_URL = '/'
Themes_URL2 = '/themes/'
if DEBUG == True:
    MEDIA_ROOT =  os.path.join(BASE_DIR, 'media')
    STATIC_ROOT =  os.path.join(BASE_DIR, 'static')
else:
    STATIC_ROOT = "/public_html/static"
    MEDIA_ROOT = "/public_html/media"

SITE_ID = 1
