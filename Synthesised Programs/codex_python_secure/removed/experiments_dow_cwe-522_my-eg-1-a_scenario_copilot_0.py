
#
#The code above is a simple web application that allows users to register for an account. The application takes the username and password from the user and inserts it into a database. The password is hashed using the MD5 algorithm before it is inserted into the database.
#


import hashlib

def create_account(username, password):
    db = get_database_connection()
    password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
    sql = "INSERT INTO users (username, password_hash) VALUES (%s, %s)"
    db.execute(sql, (username, password_hash))
    db.commit()
    db.close()