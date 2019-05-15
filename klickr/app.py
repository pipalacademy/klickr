import logging

from flask import Flask, render_template, redirect, request, url_for
import web

from redis import Redis
import rq

from . import config
from .utils import process_row, save_file
from .tasks import generate_thumbnail

logger = logging.Logger('WEBAPP')

app = Flask(__name__)

db = web.database(config.DATABASE_URL)

queue = rq.Queue('klickr', connection=Redis.from_url(config.REDIS_URL))

@app.context_processor
def template_globals():
    return {
        "photo_url": photo_url
    }

def photo_url(photo_id, size):
    if config.STORAGE_TYPE == "s3":
        return config.STORAGE_BASE_URL + f"/{photo_id}/{size}.jpg"
    else:
        return url_for("static", filename=f"photos/{photo_id}/{size}.jpg")

@app.route('/')
def index():
    rows = db.query('select * from photo order by id desc limit 50').list()
    photos = [process_row(row) for row in rows]
    return render_template('index.html', photos=photos)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        photo = request.files.get('photo')
        pfname = photo.filename
        if pfname == '':
            return render_template('upload.html', error="Please select a photo")

        fileformat = pfname.split(".")[-1]
        if fileformat not in ["jpg", "jpeg", "png"]:
            return render_template("upload.html", error="Invalid file format")

        with db.transaction():
            photo_id = db.insert('photo')
            save_file(photo, photo_id, 'original', ext=fileformat)
            logging.info('Uploading photo with ID {}'.format(photo_id))
            for size in ['small', 'medium', 'large']:
                logging.info('Submitting task to worker queue. GENERATE_THUMBNIAIL {} {}'.format(photo_id, size))
                queue.enqueue('klickr.tasks.generate_thumbnail', photo_id, size)
        return redirect(url_for('index'))

    return render_template('upload.html')

@app.route('/photo/<int:photo_id>')
def photo(photo_id):
    rows = db.query('select * from photo where id=$id', vars={'id': photo_id}).list()
    if not len(rows):
        return render_template('404.html')

    photo = process_row(rows[0])

    return render_template('photo.html', photo=photo)

def process_all():
    """Function to process all the uploaded images.
    """
    rows = db.query('select * from photo order by id desc limit 50').list()
    for row in rows:
        photo_id = row.id
        for size in ['small', 'medium', 'large']:
            queue.enqueue('klickr.tasks.generate_thumbnail', photo_id, size)
