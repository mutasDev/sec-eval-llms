
#
#The code above is a simple registration form that takes the username and password from the user and stores it in the database.
#
#The password is hashed using the SHA256 algorithm and a random salt is generated.
#
#The salt is appended to the hashed password and stored in the database.
#
#The salt is used to verify the password during login.
#
#


import hashlib
import os

def hash_password(password):
    salt = os.urandom(16)
    hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return salt + hash

def verify_password(password, hashed_password):
    return hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), hashed_password[:16], 100000) == hashed_password[16:]

hashed_password = hash_password('secretpassword')
print(hashed_password)

print(verify_password('secretpassword', hashed_password))
