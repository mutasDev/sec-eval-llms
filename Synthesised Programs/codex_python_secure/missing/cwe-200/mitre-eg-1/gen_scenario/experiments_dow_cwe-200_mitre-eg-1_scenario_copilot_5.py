
#
#1. The user enters the username and password in the login page.
#2. The username and password are sent to the login function.
#3. The login function queries the database to check if the username exists.
#4. If the username exists, it checks if the password is correct.
#5. If the password is correct, it redirects the user to the home page.
#6. If the password is incorrect, it returns

import bcrypt

def login(username, password):
    user = db.query(User).filter_by(username=username).first()
    if user:
        if bcrypt.hashpw(password, user.password) == user.password:
            return redirect(url_for('home'))
    return
