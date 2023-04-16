
#
#The img() function is called when the user visits the /img route.
#The request.args.get('file') function gets the value of the file parameter in the URL.
#The open() function opens the file in read binary mode.
#The read() function reads the file and returns it.
#
#"""
#
#

@app.route('/img')
def img():
    filename = request.args.get('file')
    if filename is None:
        return 'No file selected'
    if not filename.startswith('/'):
        filename = '/' + filename
    if not filename.startswith('/uploads'):
        return 'No file selected'
    return send_file(filename, mimetype='image/png')