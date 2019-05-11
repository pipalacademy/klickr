import os

DATABASE_URL = os.getenv('DATABASE_URL', 'postgres:///klickr')
REDIS_URL = os.getenv('REDIS_URL', 'redis://')

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_DEFAULT_REGION = os.getenv("AWS_DEFAULT_REGION", "us-east-1")
AWS_ENDPOINT_URL = os.getenv("AWS_ENDPOINT_URL")
S3_BUCKET = os.getenv("S3_BUCKET", "klickr-pal-test")
