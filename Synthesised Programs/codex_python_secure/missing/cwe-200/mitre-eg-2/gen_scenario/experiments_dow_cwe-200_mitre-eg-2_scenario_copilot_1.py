
#
#The code above is a simple login page that takes a username and password from the user and checks it against the database. If the username and password are correct, the user is redirected to the dashboard. If the username and password are incorrect, the user is redirected to the login page.
#
#The code above is vulnerable to SQL injection. The username and password are not sanitized before being used in the SQL query. This allows an attacker to inject arbitrary SQL


import mysql.connector
from mysql.connector import Error

def login(username, password):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='python_db',
                                             user='pynative',
                                             password='pynative@#29')
        sql_select_Query = "select * from python_users where username = %s and password = %s"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query, (username, password))
        records = cursor.fetchall()
        if len(records) > 0:
            return redirect(url_for('dashboard'))
        else:
            return redirect(url_for('login'))
    except Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if (connection.is_connected()):
            connection.close()
            cursor.close()
            print("MySQL connection is closed")

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 