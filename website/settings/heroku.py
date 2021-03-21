import os

from website.settings.base import *

import dj_database_url

SECRET_KEY = get_sescret_setting("SECRET_KEY")
DEBUG = False
ALLOWED_HOSTS = [get_sescret_setting("HOST")]

#Config database
DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)

#Config for server static files in heroku
MIDDLEWARE.insert(0, "whitenoise.middleware.WhiteNoiseMiddleware")
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

#Security
SECURE_SSL_REDIRECT = True
# SECURE_HSTS_SECONDS
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
