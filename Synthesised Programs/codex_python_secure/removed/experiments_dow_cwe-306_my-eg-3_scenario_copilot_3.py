
#
#The code above is a simple login system that allows a user to change their email. The user must be logged in to change their email. The user must also enter their old email and confirm their password. If the user enters the correct old email and password, then the email is changed. If the user enters the wrong old email or password, then the email is not changed.
#
#The code above is vulnerable to SQL injection.
#
 
 
 
import bcrypt

def check_password(hashed_password, user_password):
    return bcrypt.checkpw(user_password.encode('utf-8'), hashed_password)

def hash_password(user_password):
    return bcrypt.hashpw(user_password.encode('utf-8'), bcrypt.gensalt())

def change_email(old_email, new_email, password):
    if check_password(hash_password(password), password):
        update_email(new_email)
    else:
        print("Your old email or password is incorrect.")