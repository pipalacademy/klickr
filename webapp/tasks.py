from PIL import Image

from . import config

SIZE_MAP = {
    'small': (128, 128),
    'medium': (256, 256),
    'large': (512, 512)
}

def get_path(photo_id):
    return config.UPLOADS_FOLDER.rstrip('/') + '/' + f'{photo_id}/original.jpg'

def generate_thumbnail(photo_id, size):
    original_path = get_path(photo_id)
    image = Image.open(original_path)
    image.thumbnail(SIZE_MAP[size])
    image.save(original_path.replace('original', size))
