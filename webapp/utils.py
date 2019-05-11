import boto3

from . import config

s3 = boto3.client(
    's3',
    aws_access_key_id=config.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY,
    region_name=config.AWS_DEFAULT_REGION,
    endpoint_url=config.AWS_ENDPOINT_URL
)

def process_row(row):
    photo_id = row.id
    data = {
        'id': photo_id
    }

    for size in ['original', 'small', 'medium', 'large']:
        data[f'{size}_url'] = get_signed_url(f'photos/{photo_id}/{size}.jpg')

    return data

def get_signed_url(path, expires_in=300):
    return s3.generate_presigned_url('get_object',
        ExpiresIn=expires_in,
        Params={
            'Bucket': config.S3_BUCKET,
            'Key': path
        })
