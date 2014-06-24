# This is the settings file used by your live production server(s).
# That is, the server(s) that host the real live website.
# This file contains production-level settings only. It is sometimes called prod.py
import os
from django.core.exceptions import ImproperlyConfigured

from .base import *

# Parse database configuration from $DATABASE_URL
import dj_database_url

DATABASES['default'] = dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

def get_env_variable(var_name):
    """
      Get the environment variable or return exception
    """
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the %s environment variable" % var_name
        raise ImproperlyConfigured(error_msg)

SECRET_KEY = get_env_variable("DJANGO_SECRET_KEY")