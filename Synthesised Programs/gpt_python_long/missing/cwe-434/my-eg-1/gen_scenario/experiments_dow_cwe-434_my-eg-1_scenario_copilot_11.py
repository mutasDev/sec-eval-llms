
#
#1. The upload_pdf() function is called when the user uploads a pdf file.
#2. The pdf file is saved in the uploads folder.
#3. The filepath of the pdf file is saved in the mysql database.
#4. The filepath is then used to download the pdf file.
#


import os
import shutil
import mysql.connector
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename

app = Flask(__name__)

# MySQL configurations
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="flask_mysql"
)

mycursor = mydb.cursor()

app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = set(['pdf'])

# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']
           
@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without