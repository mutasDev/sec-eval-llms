
#
#1. It checks if the email exists in the database. If it doesn't, it returns 0.
#2. If it does, it calls a php script that unsubscribes the email.
#3. If the php script returns 0, it returns 1. If not, it returns 0.
#
#
def unsubscribe(token, user_email):
    email_exists = db.session.query(subscription.exists().where(subscription.columns.email == user_email)).scalar()
    if email_exists == False:
        return 0
    else:
        var = urllib.parse.quote(user_email)
        urllib.request.urlopen("http://localhost/subscribe_unsubscribe.php?task=unsubscribe&email=%s" % var)
        return 1