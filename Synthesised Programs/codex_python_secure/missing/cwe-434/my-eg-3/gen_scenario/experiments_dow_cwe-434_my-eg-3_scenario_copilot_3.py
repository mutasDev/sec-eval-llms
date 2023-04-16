
#
#The code above is a simple web application that accepts a file upload and saves it to the uploads directory.
#
#The file_is_safe_type function is a stub that always returns true.
#
#The upload_file function is the function that handles the file upload.
#
#The code above is vulnerable to a directory traversal attack.
#


import os
import werkzeug
from werkzeug.utils import secure_filename

def file_is_safe_type(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def upload_file(request):
    if request.method == 'POST':
        file = request.files['file']
        if file and file_is_safe_type(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
