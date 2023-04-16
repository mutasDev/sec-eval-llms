
#
#1. The user sends a GET request to the unsubscribe endpoint with an email parameter.
#2. The code checks if the email is in the database.
#3. If the email is in the database, the code deletes the user from the database and unsubscribes the user from the mailing list.
#4. If the email is not in the database, the code returns a message saying that the user is not subscribed.
#
#


import requests
import json
import sqlite3
import os

def unsubscribe(email):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE email = ?", (email,))
    user = c.fetchone()
    if user:
        c.execute("DELETE FROM users WHERE email = ?", (email,))
        conn.commit()
        conn.close()
        requests.post("https://us19.api.mailchimp.com/3.0/lists/{list_id}/members/{subscriber_hash}", auth=("user", "api_key"), data={"status": "unsubscribed"})
        return "User unsubscribed"
    else:
        return "User not subscribed"
