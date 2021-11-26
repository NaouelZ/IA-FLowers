# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import flask
import os
import NN

from flask import request, jsonify, render_template, flash, redirect, url_for
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = flask.Flask(__name__)
app.config["DEBUG"] = False


app.config["UPLOAD_FOLDER"] = "static/"

@app.route('/')
def upload_file():
    return render_template('index.html')


@app.route('/display', methods = ['GET', 'POST'])
def save_file():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)

        f.save(app.config['UPLOAD_FOLDER'] + filename)
        url = "static/" + filename
        print(filename)
        
    return render_template('content.html', url = url, content = NN.test_model(filename)) 


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug = True)
