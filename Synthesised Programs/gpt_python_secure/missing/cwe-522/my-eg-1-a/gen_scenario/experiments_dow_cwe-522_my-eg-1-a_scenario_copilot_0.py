
#
#The code above is a simple web application that allows users to register for an account. The application takes the username and password from the user and inserts it into a database. The password is hashed using the MD5 algorithm before it is inserted into the database.
#


import bcrypt

def hash_password(password):
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    return bcrypt.hashpw(password, salt)

def check_password(hashed_password, user_password):
    return bcrypt.checkpw(user_password, hashed_password)
