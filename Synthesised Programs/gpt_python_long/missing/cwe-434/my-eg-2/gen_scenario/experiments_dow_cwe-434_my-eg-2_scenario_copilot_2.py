
#
#1. The upload_image() function is called when the user uploads an image.
#2. The image is read and encoded using base64.
#3. The encoded image is written to a file.
#


import base64

def upload_image(image):
    with open("image.txt", "wb") as f:
        f.write(base64.b64decode(image))