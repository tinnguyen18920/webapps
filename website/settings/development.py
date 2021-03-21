import os

from website.settings.base import *

SECRET_KEY = '!7!r52%c+c5_2ps096j$0rxv*6(&%6$2a#u*4_))xre(!%5#9!'
DEBUG = os.getenv("DEUBG") != '0'
ALLOWED_HOSTS = ['*']

#For test heroku DATABASE
if os.getenv("DATABASE_URL"):
    import dj_database_url
    DATABASES['default'] = dj_database_url.config()