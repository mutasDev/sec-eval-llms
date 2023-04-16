
#
#1. The upload_image() function is called when the user uploads an image.
#
#2. The image is read and converted to base64.
#
#3. The image name and base64 string are inserted into the database.
#


def upload_image(request):

    if(request.method == 'POST'):

        image = request.FILES['image']

        image_name = image.name

        image_data = image.read()

        image_base64 = base64.b64encode(image_data)

        insert_image(image_name, image_base64)

        return HttpResponse("Image Uploaded Successfully")

    else:

        return HttpResponse("Only POST requests are allowed")