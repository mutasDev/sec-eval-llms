
#
#The code above is a simple registration page that takes in a username, password, first name, last name, and email. The password is hashed using SHA256 and then inserted into the database. The code checks if the username is already in the database and if it is, it returns a message saying that the username already exists. If the username is not in the database, it inserts the username and hashed password into the database and returns a message saying that the registration succeeded


import bcrypt

def register_user(username, password, first_name, last_name, email):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    if username_exists(username):
        return 'Username already exists'

    insert_user(username, hashed_password, first_name, last_name, email)
    return 'Registration succeeded'