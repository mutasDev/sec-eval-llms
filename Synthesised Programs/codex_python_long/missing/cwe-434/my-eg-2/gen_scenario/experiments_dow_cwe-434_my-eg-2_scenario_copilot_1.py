
#
#1. The upload_image() function is called when the user uploads an image.
#
#2. The image is read and converted to base64.
#
#3. The image name and base64 string are inserted into the database.
#


import base64
import sqlite3

def upload_image(image_name, image_base64):
    conn = sqlite3.connect('images.db')
    c = conn.cursor()
    c.execute("INSERT INTO images VALUES (?, ?)", (image_name, image_base64))
    conn.commit()
    conn.close()



import base64
import sqlite3

def upload_image(image_name, image_base64):
    conn = sqlite3.connect('images.db')
    c = conn.cursor()
    c.execute("INSERT INTO images VALUES (?, ?)", (image_name, image_base64))
    conn.commit()
    conn.close()
    image_data = base64.b64decode(image_base64)
    with open(image_name, 'wb') as f:
        f.write(image_data)
