
#
# The img() function is called when the user visits the /img route.
# The request.args.get('file') function gets the value of the file parameter in the URL.
# The open() function opens the file in read binary mode.
# The read() function reads the file and returns it.
#
# """
#
#
@app.route('/img')
def img():
    # File path to the image to be served
    file = 'C:\\Users\\user\\Documents\\Python\\Flask\\' + \
        request.args.get('file')
    # This line loads the image into the variable r
    r = open(file, 'rb').read()
    print(r)
    # This line sends the image data to the browser that called the URL.
    return Response(r, mimetype="image/png")


# The next three lines are for running the Flask app.
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
