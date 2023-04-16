
#
#The code above is a simple web application that allows users to register for an account. The application takes the username and password from the user and inserts it into a database. The password is hashed using the MD5 algorithm before it is inserted into the database.
#

import hashlib
import MySQLdb

def register(username, password):
    password = hashlib.md5(password).hexdigest()
    db = MySQLdb.connect(host="localhost", user="root", passwd="", db="test")
    cursor = db.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
    db.commit()
    db.close()

register("admin", "admin")