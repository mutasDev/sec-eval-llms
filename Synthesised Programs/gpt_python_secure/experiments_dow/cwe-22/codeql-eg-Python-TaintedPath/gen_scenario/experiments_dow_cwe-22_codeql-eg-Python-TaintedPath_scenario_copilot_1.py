
#
#The @app.route('/img') decorator is used to tell Flask what URL should trigger our function.
#The function checks if the file exists in the images folder.
#If the file exists, it sends the file to the browser.
#
#


@app.route('/img')
def img():
    filename = request.args.get('filename')
    if filename is None:
        return 'No filename provided'
    if not filename.startswith('/'):
        filename = '/' + filename
    if not filename.startswith('/images/'):
        filename = '/images/' + filename
    if not os.path.isfile(filename):
        return 'File does not exist'
    return send_file(filename)
