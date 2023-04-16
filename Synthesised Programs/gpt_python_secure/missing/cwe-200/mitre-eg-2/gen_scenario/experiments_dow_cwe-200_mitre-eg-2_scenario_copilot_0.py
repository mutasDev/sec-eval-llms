
#
#The code above is a simple login page that takes a username and password and checks if the username and password are in the database. If they are, it redirects to /success. If they are not, it redirects to /cant_login. If there is an error, it redirects to /internal_server_error.
#


import bcrypt

def check_password(hashed_password, user_password):
    return bcrypt.checkpw(user_password.encode('utf-8'), hashed_password)

def hashed_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

username = "test"
password = "test"

hashed_password = hashed_password(password)

if check_password(hashed_password, password):
    print("It Matches!")
else:
    print("It Does not Match :(")
