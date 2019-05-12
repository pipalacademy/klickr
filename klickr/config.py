import os

DATABASE_URL = os.getenv('DATABASE_URL', 'postgres:///klickr')
REDIS_URL = os.getenv('REDIS_URL', 'redis://')

UPLOADS_FOLDER = os.getenv('UPLOADS_FOLDER', 'klickr/static/photos')
