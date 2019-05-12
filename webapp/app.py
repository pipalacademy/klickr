from flask import Flask, render_template, redirect, request, url_for
import web

from . import config
from .utils import process_row, save_file

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
        if pfname == '':
            return render_template('upload.html')
        if pfname.split('.')[-1].lower() not in ['jpg', 'jpeg']:
            return render_template('upload.html')

        photo_id = db.insert('photo')
        save_file(photo, photo_id, 'original')
        return redirect(url_for('index'))

    return render_template('upload.html')

@app.route('/photo/<int:photo_id>')
def photo(photo_id):
    rows = db.query('select * from photo where id=$id', vars={'id': photo_id}).list()
    if not len(rows):
        return render_template('404.html')

    photo = process_row(rows[0])

    return render_template('photo.html', photo=photo)
