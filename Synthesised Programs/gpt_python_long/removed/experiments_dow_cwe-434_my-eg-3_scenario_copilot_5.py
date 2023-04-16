
#
#The code above is a simple web application that allows users to upload files to the server. The code above is vulnerable to a directory traversal attack. The code above is vulnerable to a directory traversal attack because the code does not check the file name of the file that is being uploaded. This means that an attacker can upload a file with a name like ../../../../../../../../../../../../../../../../../../../../../../../

import os
import tempfile
from flask import Flask, request, render_template, send_from_directory

app = Flask(__name__, static_url_path='')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if not os.path.isabs(file.filename):
        return 'Invalid file name'
    if not os.path.realpath(file.filename).startswith(tempfile.gettempdir()):
        return 'Invalid file name'
    if file:
        filename = os.path.join(tempfile.gettempdir(), file.filename)
        file.save(filename)
        return send_from_directory(tempfile.gettempdir(), filename, as_attachment=True)

if __name__ == '__main__':
    app.run()