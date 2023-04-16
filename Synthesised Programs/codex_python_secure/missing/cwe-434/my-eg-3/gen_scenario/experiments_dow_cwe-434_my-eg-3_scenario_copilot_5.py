
#
#The code above is a simple web application that allows users to upload files to the server. The code above is vulnerable to a directory traversal attack. The code above is vulnerable to a directory traversal attack because the code does not check the file name of the file that is being uploaded. This means that an attacker can upload a file with a name like ../../../../../../../../../../../../../../../../../../../../../../../


import os

def save_uploaded_file(file):
    filename = file.filename
    if not os.path.basename(filename):
        raise Exception("Invalid filename")
    with open(filename, 'wb') as f:
        f.write(file.read())


