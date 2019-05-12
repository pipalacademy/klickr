from flask import Flask, render_template, redirect, request, url_for
import web

from . import config
from .utils import process_row, upload_file

app = Flask(__name__)

db = web.database(config.DATABASE_URL)

@app.route('/')
def index():
    rows = db.query('select * from photo limit 50;').list()
    photos = [process_row(row) for row in rows]
    return render_template('index.html', photos=photos)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        photo = request.files.get('photo')
        pfname = photo.filename
        photo_id = db.insert('photo', metadata='klickr')
        print(photo_id)
        upload_file(photo, photo_id, 'original')
        return redirect(url_for('index'))

    return render_template('upload.html')
