
#
#1. The upload_image() function is called when the user uploads an image.
#
#2. The image is read and converted to base64.
#
#3. The image name and base64 string are inserted into the database.
#



def upload_image():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            with open(os.path.join(app.config['UPLOAD_FOLDER'], filename), "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read())
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            db.session.add(Image(name=filename, data=encoded_string))
            db.session.commit()
            return redirect(url_for('uploaded_file', filename=filename))
    return '''
    &lt;!doctype html&gt;
    &lt;title&gt;Upload new File&lt;/title&gt;
    &lt;h1&gt;Upload new File&lt;/h1&gt;
    &lt;form method=post enctype=multipart/form-data&gt;
      &lt;p&gt;&lt;input type=file name=file&gt;
         &lt;'''