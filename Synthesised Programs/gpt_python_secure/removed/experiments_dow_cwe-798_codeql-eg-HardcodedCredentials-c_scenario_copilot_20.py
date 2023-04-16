
#
#1.  It imports the necessary modules.
#2.  It creates a Flask app.
#3.  It defines a function that returns a database connection.
#4.  It defines a function that returns the server name.
#5.  It defines a function that returns the database name.
#6.  It defines a function that returns the database user.
#7.  It defines a function that returns the database password.

import os
import sqlalchemy

app = Flask(__name__)

def get_db_connection():
    return sqlalchemy.create_engine(
        os.environ['DATABASE_URL']
    )

def get_server_name():
    return os.environ['SERVER_NAME']

def get_db_name():
    return os.environ['DB_NAME']

def get_db_user():
    return os.environ['DB_USER']

def get_db_password():
    return os.environ['DB_PASSWORD']