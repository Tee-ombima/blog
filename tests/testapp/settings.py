import os
from puput import PUPUT_APPS
from dotenv import load_dotenv
from django.core.management.utils import get_random_secret_key
import dj_database_url



load_dotenv()

WAGTAIL_SITE_NAME = "Puput blog"
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", get_random_secret_key())
DEBUG = False
ALLOWED_HOSTS=['*']
DATABASE_URL = os.getenv("DATABASE_URL")
# ALLOWED_HOSTS =['127.0.0.1','wfspotlight.herokuapp.com','localhost','www.spotlightkenya.club','spotlightkenya.club']
#default_csrf_trusted_origins = "http://127.0.0.1,https://127.0.0.1,http://localhost,https://localhost,https://SpotlightKenya.ngrok.io"
CSRF_TRUSTED_ORIGINS=['https://b44d-197-248-108-89.ngrok-free.app','http://127.0.0.1','https://www.spotlightkenya.club/','https://spotlightkenya.club/']
INSTALLED_APPS = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "storages",
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
        'PORT': '5432'
    }
}
DATABASES['default'] = dj_database_url.config(conn_max_age=10000, ssl_require=True)



WAGTAILADMIN_BASE_URL = '/blog_admin'


LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_ROOT = "/tmp/static"
#STATIC_URL = "/static/"
MEDIA_ROOT = "/tmp/media"
#MEDIA_URL = "/media/"

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]


DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_LOCATION = 'media'
STATIC_URL = f'https://spotlightkenya.sgp1.digitaloceanspaces.com/static/'
MEDIA_URL = f'https://spotlightkenya.sgp1.digitaloceanspaces.com/media/'


AWS_S3_ENDPOINT_URL = 'https://spotlightkenya.sgp1.digitaloceanspaces.com'  # Replace your-region with the region where your bucket is located
AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_ACCESS_KEY_ID="DO00WBEEMAQWJ4FZCGLX"
AWS_SECRET_ACCESS_KEY="hx0HQ6vEKqP2eW/AICZcWBCg5JfSQBSPEj8tc+f5ERI"
AWS_STORAGE_BUCKET_NAME='spotlightkenya'
