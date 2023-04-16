
#
#The code above is a simple login page that takes the username and password from the user and checks if the username and password are correct. If they are correct, the user is redirected to the session page. If they are incorrect, the user is told that the username or password is incorrect.
#


import hashlib

def login(username, password):
    """

This function takes the username and password from the user and checks if the username and password are correct. If they are correct, the user is redirected to the session page. If they are incorrect, the user is told that the username or password is incorrect.

"""

    password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()

    if username == 'admin' and password_hash == '21232f297a57a5a743894a0e4a801fc3':
        print("Login successful!")
    else:
        print("Incorrect username or password!")