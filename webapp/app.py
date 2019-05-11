from flask import Flask, render_template, redirect, request
import web

from . import config
from .utils import process_row

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
        # form = request.form
        # do something
        return redirect(url_for('upload'))

    return render_template('upload.html')
