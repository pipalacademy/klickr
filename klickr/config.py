import os

DATABASE_URL = os.getenv('DATABASE_URL', 'postgres:///klickr')
REDIS_URL = os.getenv('REDIS_URL', 'redis://')

# 2 types of storage are supported: disk and s3
STORAGE_TYPE = os.getenv("STORAGE_TYPE", "disk")

STORAGE_S3_BUCKET = os.getenv("STORAGE_S3_BUCKET")
STORAGE_S3_BASE_URL = os.getenv("STORAGE_S3_BASE_URL")

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_ENDPOINT_URL = os.getenv("AWS_ENDPOINT_URL")
AWS_REGION_NAME = os.getenv("AWS_REGION_NAME")


UPLOADS_FOLDER = os.getenv('UPLOADS_FOLDER', 'klickr/static/photos')
