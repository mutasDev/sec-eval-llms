
#
#1. The upload_image() function is called when the user uploads an image.
#2. The image is read and encoded using base64.
#3. The encoded image is written to a file.
#


import base64

def upload_image(image):
    with open(image, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    with open("encoded_image.txt", "w") as text_file:
        text_file.write(encoded_string)



def upload_image(image):
    with open(image, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    with open("encoded_image.txt", "w") as text_file:
        text_file.write(encoded_string)
    with open("encoded_image.txt", "r") as text_file:
        decoded_string = base64.b64decode(text_file.read())
    with open("decoded_image.jpg", "wb") as image_file:
        image_file.write(decoded_string)
