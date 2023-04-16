
#
#The code above is a simple registration form that takes in a username and password. The password is then hashed using the pbkdf2_hmac algorithm. The salt is generated using the os.urandom function. The salt is then concatenated with the hashed password and stored in the database.
#


import os
import hashlib

def hash_password(password):
    """Hash a password for storing."""
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac('sha256', password, salt, 100000)
    return salt + key

def verify_password(hashed_password, provided_password):
    """Verify a stored password against one provided by user"""
    salt = hashed_password[:32]
    key = hashed_password[32:]
    new_key = hashlib.pbkdf2_hmac('sha256', provided_password, salt, 100000)
    return new_key == key