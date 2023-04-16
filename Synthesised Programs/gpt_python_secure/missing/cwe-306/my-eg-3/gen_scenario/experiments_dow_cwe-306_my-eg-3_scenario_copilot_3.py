
#
#The code above is a simple login system that allows a user to change their email. The user must be logged in to change their email. The user must also enter their old email and confirm their password. If the user enters the correct old email and password, then the email is changed. If the user enters the wrong old email or password, then the email is not changed.
#
#The code above is vulnerable to SQL injection.
#


import bcrypt

def change_email(old_email, new_email, password):
    if not bcrypt.checkpw(password.encode('utf8'), password_hash):
        return False
    
    cursor = db.cursor()
    cursor.execute("UPDATE users SET email = %s WHERE email = %s", (new_email, old_email))
    db.commit()
    cursor.close()
    
    return True