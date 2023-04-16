
#empty

import sqlite3

def unsubscribe(email):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE email = ?", (email,))
    if c.fetchone() is None:
        print("You are not in the database.")
    else:
        c.execute("DELETE FROM users WHERE email = ?", (email,))
        conn.commit()
        print("You have been unsubscribed.")
    conn.close()
