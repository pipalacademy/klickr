from PIL import Image
import os
import logging
from . import config
from .utils import get_s3_client

logger = logging.getLogger('WORKER')

SIZE_MAP = {
    'small': (128, 128),
    'medium': (256, 256),
    'large': (512, 512)
}

def get_path(photo_id):
    return os.path.join(config.UPLOADS_FOLDER, str(photo_id), 'original.jpg')

def generate_thumbnail(photo_id, size):
    if config.STORAGE_TYPE == "s3":
        generate_thumbnail_s3(photo_id, size)
    else:
        generate_thumbnail_disk(photo_id, size)

def generate_thumbnail_disk(photo_id, size):
    logging.info('Thumbnail of size {} requested for photo {}'.format(size, photo_id))
    original_path = get_path(photo_id)
    image = Image.open(original_path)
    image.thumbnail(SIZE_MAP[size])
    image.save(original_path.replace('original', size))
    logging.info('Thumbnail of size {} generated for photo {}'.format(size, photo_id))

def generate_thumbnail_s3(photo_id, size):
    s3 = get_s3_client()
    original_path = get_path(photo_id)
    thumb_path = original_path.replace('original', size)

    s3.download_file(config.STORAGE_S3_BUCKET, f"{photo_id}/original.{jpg}", original_path)
    generate_thumbnail_disk(photo_id, size)
    s3.upload_file(thumb_path, config.STORAGE_S3_BUCKET, f"{photo_id}/{size}.{jpg}", ExtraArgs={'ACL': 'public-read'})
    logging.info('Thumbnail of size {} saved to S3 for photo {}'.format(size, photo_id))
