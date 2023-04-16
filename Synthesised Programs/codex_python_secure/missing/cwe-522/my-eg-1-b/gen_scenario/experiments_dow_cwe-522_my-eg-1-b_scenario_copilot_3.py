
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
    # uuid is used to generate a random number
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), 
                                salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')

def verify_password(stored_password, provided_password):
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512', 
                                  provided_password.encode('utf-8'), 
                                  salt.encode('ascii'), 
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password
