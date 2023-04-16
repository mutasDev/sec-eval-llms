
"""
1. The user enters their email address into the unsubscribe form on the website.
2. The email address is passed to the unsubscribe function.
3. The unsubscribe function connects to the database and checks if the email address is in the database.
4. If the email address is in the database, it is removed.
5. If the email address is not in the database, the user is told that they are not in the database.
"""


import mysql.connector

def unsubscribe(email):
    conn = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='newsletter')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM subscribers WHERE email = %s", (email,))
    conn.commit()
    cursor.close()
    conn.close()

unsubscribe("test@example.com")