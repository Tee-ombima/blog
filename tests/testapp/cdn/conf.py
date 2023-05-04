import os

AWS_S3_REGION_NAME = os.getenv("AWS_S3_REGION_NAME", "sgp1")
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")
AWS_LOCATION = os.getenv("AWS_LOCATION", "assets")
PUBLIC_MEDIA_LOCATION = os.getenv("PUBLIC_MEDIA_LOCATION", "media")
AWS_DEFAULT_ACL = "public-read"
AWS_S3_ENDPOINT_URL = f"https://blogbucket.sgp1.digitaloceanspaces.com"
AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=86400"}

DEFAULT_FILE_STORAGE = "tests.testapp.cdn.backends.MediaRootS3Boto3Storage"
STATICFILES_STORAGE = "tests.testapp.cdn.backends.StaticRootS3Boto3Storage"


STATIC_URL = f'https://blogbucket.sgp1.digitaloceanspaces.com/static/'
MEDIA_URL = f'https://blogbucket.sgp1.digitaloceanspaces.com/media/'