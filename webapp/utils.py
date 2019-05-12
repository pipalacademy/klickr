import pathlib
from . import config

def process_row(row):
    photo_id = row.id
    data = {
        'id': photo_id
    }

    for size in ['original', 'small', 'medium', 'large']:
        data[f'{size}_url'] = f'photos/{photo_id}/{size}.jpg'

    return data

def save_file(file, photo_id, image_type):
    photo_folder = config.UPLOADS_FOLDER + f'/{photo_id}'
    photo_folder = pathlib.Path(photo_folder)

    photo_folder.mkdir(exist_ok=True)

    photo_path = photo_folder.joinpath(f'{image_type}.jpg')
    with photo_path.open('wb') as f:
        f.write(file.read())
    # file.save(photo_path)
