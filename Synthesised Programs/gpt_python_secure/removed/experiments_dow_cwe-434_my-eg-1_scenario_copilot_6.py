
#
#1. I have a flask app that accepts a pdf file and saves it in a folder called uploads.
#
#2. I have a python script that converts the pdf file to text and saves it in a folder called text.
#
#3. I have a python script that reads the text file and saves it in a database.
#

import os

from flask import Flask, request, redirect, url_for, render_template

from werkzeug import secure_filename

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/')

def index():

    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])

def upload_file():

    if request.method == 'POST':

        file = request.files['file']

        if file:

            filename = secure_filename(file.filename)

            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            return redirect(url_for('uploaded_file',

                                    filename=filename))

    return render_template('upload.html')

@app.route('/uploads/<filename>')

def uploaded_file(filename):

    return render_template('uploaded.html', filename=filename)

if __name__ == '__main__':

    app.run(

        host="0.0.0.0",

        port=int("80"),

        debug=True

)