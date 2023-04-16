
#
#1. The upload_image() function is called when the user uploads an image.
#2. The image is read and encoded using base64.
#3. The encoded image is written to a file.
#


def upload_image(request):
    if request.method == 'POST':
        image = request.FILES['image']
        if image:
            encoded_image = base64.b64encode(image.read())
            with open('/tmp/image.txt', 'wb') as f:
                f.write(encoded_image)
