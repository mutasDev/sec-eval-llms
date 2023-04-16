
#
#The file_is_safe_type function is a function that checks if the file is safe to upload.
#
#The upload_file function is the function that handles the upload of the file.
#
#The f.save(os.path.join('uploads', filename)) line saves the file to the uploads folder.
#
#The uploads folder is created in the same directory as the source file.
#
#


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and file_is_safe_type(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join('uploads', filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''





































































































































































































