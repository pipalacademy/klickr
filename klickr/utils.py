import pathlib
from PIL import Image
from . import config
import boto3

def process_row(row):
    photo_id = row.id
    data = {
        'id': photo_id
    }

    for size in ['original', 'small', 'medium', 'large']:
        data[f'{size}_url'] = f'photos/{photo_id}/{size}.jpg'

    return data

s3_client = None
def get_s3_client():
    global s3_client
    if s3_client is None:
        s3_client = boto3.client('s3',
            aws_access_key_id=config.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY,
            endpoint_url=config.AWS_ENDPOINT_URL,
            region_name=config.AWS_REGION_NAME)
    return s3_client

def save_file(file, photo_id, image_type, ext="jpg"):
    photo_folder = config.UPLOADS_FOLDER + f'/{photo_id}'
    photo_folder = pathlib.Path(photo_folder)

    photo_folder.mkdir(exist_ok=True, parents=True)

    photo_path = photo_folder.joinpath(f'{image_type}.{ext}')
    with photo_path.open('wb') as f:
        f.write(file.read())

    if config.STORAGE_TYPE == "s3":
        get_s3_client().upload_file(photo_path, config.STORAGE_S3_BUCKET, f"{photo_id}/{image_type}.{ext}", ExtraArgs={'ACL': 'public-read'})

    if ext != "jpg":
        new_path = photo_path.with_suffix(".jpg")
        image = Image.open(photo_path)
        image.convert("RGB").save(new_path)

        if config.STORAGE_TYPE == "s3":
            get_s3_client().upload_file(new_path, config.STORAGE_S3_BUCKET, f"{photo_id}/{image_type}.jpg", ExtraArgs={'ACL': 'public-read'})
