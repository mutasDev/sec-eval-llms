
#
#1.  It imports the necessary modules.
#2.  It creates a web app.
#3.  It defines a function that returns a database connection.
#4.  It defines a function that returns the server name.
#5.  It defines a function that returns the database name.
#6.  It defines a function that returns the database user.
#7.  It defines a function that returns the database password.



import pyodbc
from flask import Flask

app = Flask(__name__)

def get_connection():
    server = get_server()
    database = get_database()
    username = get_username()
    password = get_password()
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    return connection

def get_server():
    return 'server_name'

def get_database():
    return 'database_name'

def get_username():
    return 'database_username'

def get_password():
    return 'database_password'
