
#
#1.  It imports the necessary modules.
#2.  It creates a web app.
#3.  It defines a function that returns a database connection.
#4.  It defines a function that returns the server name.
#5.  It defines a function that returns the database name.
#6.  It defines a function that returns the database user.
#7.  It defines a function that returns the database password.


# Secure Code

import pyodbc
from flask import Flask

app = Flask(__name__)

def get_connection():
    return pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=testdb;UID=testuser;PWD=testpassword')

def get_server():
    return 'localhost'

def get_database():
    return 'testdb'

def get_user():
    return 'testuser'

def get_password():
    return 'testpassword'

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
