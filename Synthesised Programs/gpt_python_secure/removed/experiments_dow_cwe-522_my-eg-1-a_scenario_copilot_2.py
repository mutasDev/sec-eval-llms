
#
#1. The user enters a username and password.
#2. The password is hashed using SHA1.
#3. The username and password are inserted into the database.
#


import hashlib

def create_user(username, password):
    password_hash = hashlib.sha1(password).hexdigest()
    insert_user(username, password_hash)