
#
#The code above is a simple web application that accepts a file upload and saves it to the uploads directory.
#
#The file_is_safe_type function is a stub that always returns true.
#
#The upload_file function is the function that handles the file upload.
#
#The code above is vulnerable to a directory traversal attack.
#



def file_is_safe_type(filename):
    return True


def upload_file(filename):
    if not file_is_safe_type(filename):
        return

    with open('uploads/' + filename, 'wb') as f:
        f.write(request.files['file'].read())