
#
#The code above is a simple login page that allows a user to change their email. The user must be logged in to change their email. The user must also enter their old email, new email, and confirm password. The user must also enter the correct password to change their email. The user must also enter a new email that is different from their old email.


def change_email(self, old_email, new_email, password):
    if not self.is_logged_in():
        raise Exception("You must be logged in to change your email.")

    if not old_email:
        raise Exception("You must enter your old email.")

    if not new_email:
        raise Exception("You must enter a new email.")

    if not password:
        raise Exception("You must enter your password.")

    if new_email == old_email:
        raise Exception("Your new email must be different from your old email.")

    if not self.is_password_correct(password):
        raise Exception("Your password is incorrect.")

    self.email = new_email
    self.save()