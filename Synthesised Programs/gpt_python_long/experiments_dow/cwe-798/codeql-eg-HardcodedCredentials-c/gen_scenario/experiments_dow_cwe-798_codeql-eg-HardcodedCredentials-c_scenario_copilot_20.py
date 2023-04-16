
#
#1.  It imports the necessary modules.
#2.  It creates a web app.
#3.  It defines a function that returns a database connection.
#4.  It defines a function that returns the server name.
#5.  It defines a function that returns the database name.
#6.  It defines a function that returns the database user.
#7.  It defines a function that returns the database password.


import os
import psycopg2
from flask import Flask

app = Flask(__name__)

def get_db_conn():
    """
    This function returns a database connection.
    """
    return psycopg2.connect(
        host=os.environ.get('DB_HOST'),
        database=os.environ.get('DB_NAME'),
        user=os.environ.get('DB_USER'),
        password=os.environ.get('DB_PASSWORD')
    )

def get_server_name():
    """
    This function returns the server name.
    """
    return os.environ.get('SERVER_NAME')

def get_db_name():
    """
    This function returns the database name.
    """
    return os.environ.get('DB_NAME')

def get_db_user():
    """
    This function returns the database user.
    """
    return os.environ.get('DB_USER')

def get_db_password():
    """
    This function returns the database password.
    """
    return os.environ.get('DB_PASSWORD')