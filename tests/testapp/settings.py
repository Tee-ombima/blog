import os
from puput import PUPUT_APPS
from dotenv import load_dotenv
from django.core.management.utils import get_random_secret_key
import dj_database_url



load_dotenv()


WAGTAIL_SITE_NAME = "Puput blog"
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", get_random_secret_key())
DEBUG = True
#ALLOWED_HOSTS=['*']
DATABASE_URL = os.getenv("DATABASE_URL")
ALLOWED_HOSTS =['*','127.0.0.1','sea-turtle-app-fhjte.ondigitalocean.app/','localhost','www.spotlightkenya.club','spotlightkenya.club']
#default_csrf_trusted_origins = "http://127.0.0.1,https://127.0.0.1,http://localhost,https://localhost,https://SpotlightKenya.ngrok.io"
CSRF_TRUSTED_ORIGINS=['https://sea-turtle-app-fhjte.ondigitalocean.app/','http://127.0.0.1','https://www.spotlightkenya.club/','https://spotlightkenya.club/']
INSTALLED_APPS = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "storages",
    "wf_pages",
    "navigation",
    "wagtail.contrib.settings",
    
)
INSTALLED_APPS += PUPUT_APPS

MIDDLEWARE = (
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
)

ROOT_URLCONF = "tests.testapp.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "tests.testapp.wsgi.application"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DB_NAME'),
        'HOST': os.getenv('DB_HOST'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'PORT':os.getenv('PORT'),
        
    }
}
  

#DATABASES['default'] = dj_database_url.config(conn_max_age=10000, ssl_require=True)

# Overwrite the 'default' database settings with the database URL specified
# in the environment variable DATABASE_URL (if it exists).
# db_from_env = dj_database_url.config(conn_max_age=10000, ssl_require=True)
# if db_from_env:
#     DATABASES['default'].update(db_from_env)


WAGTAILADMIN_BASE_URL = '/blog_admin'


LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

from .cdn.conf import *  #noqa


STATIC_ROOT = "/tmp/static"
#STATIC_URL = "/static/"
MEDIA_ROOT = "/tmp/media"
#MEDIA_URL = "/media/"

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]







