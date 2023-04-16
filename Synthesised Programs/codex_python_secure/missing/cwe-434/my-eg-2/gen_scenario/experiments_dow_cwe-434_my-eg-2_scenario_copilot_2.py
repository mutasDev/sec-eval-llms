
#
#1. The upload_image() function is called when the user uploads an image.
#2. The image is read and encoded using base64.
#3. The encoded image is written to a file.
#

def upload_image(request):
    if request.method == 'POST':
        image = request.FILES['image']
        image_data = image.read()
        image_data = base64.b64encode(image_data)
        with open('image.txt', 'w') as f:
            f.write(image_data)
        return HttpResponse('Image Uploaded')
    else:
        return HttpResponse('Failed to Upload Image')
