
#
#The file_is_safe_type function is a function that checks if the file is safe to upload.
#
#The upload_file function is the function that handles the upload of the file.
#
#The f.save(os.path.join('uploads', filename)) line saves the file to the uploads folder.
#
#The uploads folder is created in the same directory as the python file.
#
#




def file_is_safe_type(f):
    return f.content_type in ['image/jpeg', 'image/png']


def upload_file(f):
    if not file_is_safe_type(f):
        return 'Invalid file type'
    filename = secure_filename(f.filename)
    f.save(os.path.join('uploads', filename))
    return 'Success'</code>



