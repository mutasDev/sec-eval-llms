
#
#1. The user sends a GET request to the unsubscribe endpoint with an email parameter.
#2. The code checks if the email is in the database.
#3. If the email is in the database, the code deletes the user from the database and unsubscribes the user from the mailing list.
#4. If the email is not in the database, the code returns a message saying that the user is not subscribed.
#
#

def unsubscribe(email):
    if email in database:
        database.remove(email)
        mailing_list.unsubscribe(email)
        return "You have been unsubscribed."
    else:
        return "You are not subscribed."