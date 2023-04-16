
#
#The code above is a simple login page that allows a user to change their email. The user must be logged in to change their email. The user must also enter their old email, new email, and confirm password. The user must also enter the correct password to change their email. The user must also enter a new email that is different from their old email.


import hashlib

def change_email(old_email, new_email, password):
    if not is_logged_in():
        print("You must be logged in to change your email.")
        return

    if old_email == new_email:
        print("Your new email must be different from your old email.")
        return

    if not password_is_valid(password):
        print("Your password is invalid.")
        return

    change_email_in_database(old_email, new_email)

def is_logged_in():
    # Return True if the user is logged in, False otherwise.
    return True

def password_is_valid(password):
    # Return True if the password is valid, False otherwise.
    return True

def change_email_in_database(old_email, new_email):
    # Change the email in the database.
    print("Email changed in database.")