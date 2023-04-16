
#
#1. The upload_image() function is called when the user uploads an image.
#
#2. The image is read and converted to base64.
#
#3. The image name and base64 string are inserted into the database.
#



import base64
import os
import sqlite3

def upload_image(image_name, image_data):
    conn = sqlite3.connect('images.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO images (name, data) VALUES (?, ?)", (image_name, image_data))
    conn.commit()
    cursor.close()
    conn.close()

def get_image(image_name):
    conn = sqlite3.connect('images.db')
    cursor = conn.cursor()
    cursor.execute("SELECT data FROM images WHERE name=?", (image_name,))
    image_data = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return image_data

def get_image_names():
    conn = sqlite3.connect('images.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM images")
    image_names = cursor.fetchall()
    cursor.close()
    conn.close()
    return image_names

def create_database():
    conn = sqlite3.connect('images.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE images (name TEXT, data BLOB)")
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == '__main__':
    create_database()
    image_name = 'test.png'
    image_path = os.path.join(os.getcwd(), image_name)
    with open(image_path, 'rb') as image_file:
        image_data = base64.b64encode(image_file.read())
    upload_image(image_name, image_data)
    image_data = get_image(image_name)
    with open(image_path, 'wb') as image_file:
        image_file.write(base64.b64decode(image_data))
    print(get_image_names())