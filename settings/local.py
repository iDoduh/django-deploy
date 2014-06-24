# This is the settings file that you use when you're working on the project locally.
# Local development-specific settings include DEBUG mode,
# log level, and activation of developer tools like django-debug-toolbar.

# settings/local.py
from .base import *
import dj_database_url

DEBUG = True
TEMPLATE_DEBUG = DEBUG
EMAIL_HOST = "localhost"
EMAIL_PORT = 1025

SITE_ID = 1

LANGUAGE_CODE = 'ru'

DATABASES = {
	'default': { 
    	'ENGINE': 'django.db.backends.mysql', 
    	'NAME': 'django_deploy',                     
    	'USER': 'root',
	    'PASSWORD': 'root',
	}
}
#data for db connection must be in the local virtual envoirment like DATABASE_URL=""
DATABASES['default'] =  dj_database_url.config()

SECRET_KEY = 'dasipdje1j2no3nienqdd0qw#%$^&*((UPOH'
INSTALLED_APPS += ("debug_toolbar", )
INTERNAL_IPS = ("127.0.0.1",)
MIDDLEWARE_CLASSES += ("debug_toolbar.middleware.DebugToolbarMiddleware", )
