from distutils.command.upload import upload
from flask import render_template, request
import os

UPLOAD_FOLDER = 'File Upload/static/uploads/'

def index():
    if request.method == 'POST':
        f = request.files['upload']
        f.save(os.path.join(UPLOAD_FOLDER, f.filename))
        print('File saved successfully!')
        return render_template('index.html', upload=True, fname=f.filename)
    return render_template('index.html', upload=False)