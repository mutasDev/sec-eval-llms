
#
#A decorator is used to tell Flask what URL should trigger our function.
#The function checks if the file exists in the images folder.
#If the file exists, it sends the file to the browser.
#
#

@app.route('/images/<imagename>')
def show_image(imagename):
    # find the image file name
    print(imagename)
    for root, dirs, files in os.walk("."):
        for filename in files:
            if filename == imagename:
                filepath = os.path.join(root, filename)
                image = open(filepath, "rb").read()
                b64_encoded_data = base64.b64encode(image)
                return '<img src="data:image/png;base64,{}">'.format(b64_encoded_data.decode('ascii'))
    return "image not found"