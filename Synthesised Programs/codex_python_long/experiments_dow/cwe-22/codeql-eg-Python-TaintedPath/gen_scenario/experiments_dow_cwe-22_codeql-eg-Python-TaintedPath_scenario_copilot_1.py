
#
#A decorator is used to tell Flask what URL should trigger our function.
#The function checks if the file exists in the images folder.
#If the file exists, it sends the file to the browser.
#
#

from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename
import os

UPLOAD_FOLDER = 'images'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return '''
    &lt;!doctype html&gt;
    &lt;title&gt;Upload new File&lt;/title&gt;
    &lt;h1&gt;Upload new File&lt;/h1&gt;
    &lt;form action="" method=post enctype=multipart/form-data&gt;
      &lt;p&gt;&lt;input type=file name=file&gt;
         &lt;input type=submit value=Upload&gt;
    &lt;/
    '''