
#
#1. The user enters a username and password
#2. The password is hashed using a salt
#3. The username and hashed password are inserted into the database
#


import bcrypt

def hash_password(password):
    # Hash a password for the first time
    #   (Using bcrypt, the salt is saved into the hash itself)
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(password, salt)
    return hash

def check_password(password, hashed_password):
    # Check hashed password. Useing bcrypt, the salt is saved into the hash itself
    return bcrypt.checkpw(password, hashed_password)