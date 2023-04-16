
#
#1. It checks if the email exists in the database. If it doesn't, it returns 0.
#2. If it does, it calls a php script that unsubscribes the email.
#3. If the php script returns 0, it returns 1. If not, it returns 0.
#
#
def unsubscribe(email):
    if not email_exists(email):
        return 0
    if not unsubscribe_email(email):
        return 1
    return 0