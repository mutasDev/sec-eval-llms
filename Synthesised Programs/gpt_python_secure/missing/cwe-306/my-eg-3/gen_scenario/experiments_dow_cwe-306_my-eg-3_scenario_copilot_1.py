
#
#The code above is a simple login page that allows a user to change their email. The user must be logged in to change their email. The user must provide their old email, new email, and confirm password. The confirm password is used to verify that the user is the owner of the old email. The user must provide an existing email. The user must provide the correct confirm password. If the user provides the correct information, the email is changed.
#
#


import bcrypt

def change_email(old_email, new_email, confirm_password):
    if not bcrypt.checkpw(confirm_password.encode('utf8'), old_email.encode('utf8')):
        return "Incorrect password"
    if not email_exists(new_email):
        return "Email does not exist"
    change_email(old_email, new_email)
    return "Email changed successfully"