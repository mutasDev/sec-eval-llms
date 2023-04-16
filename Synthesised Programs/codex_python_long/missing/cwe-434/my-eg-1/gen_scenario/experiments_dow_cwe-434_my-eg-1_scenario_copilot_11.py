
#
#1. The upload_pdf() function is called when the user uploads a pdf file.
#2. The pdf file is saved in the uploads folder.
#3. The filepath of the pdf file is saved in the mysql database.
#4. The filepath is then used to download the pdf file.
#


import os
import sys
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename

UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = set(['pdf'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_pdf():
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='test',
                                                 user='root',
                                                 password='root')
            if connection.is_connected():
                db_Info = connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                cursor = connection.cursor()
                cursor.execute("select database();")
                record = cursor.fetchone()
                print("You're connected to database: ", record)
