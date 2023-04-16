
#
#The code above is a simple script that accepts an image file and stores it in a MySQL database. The code is vulnerable to SQL injection.
#


import MySQLdb

def store_image(image_file):
    db = MySQLdb.connect(host="localhost", user="root", passwd="", db="test")
    cursor = db.cursor()
    cursor.execute("INSERT INTO images (image) VALUES (%s)", (image_file,))
    db.commit()
    db.close()
