
#
#The code above is a simple login page that takes a username and password from the user and checks it against the database. If the username and password are correct, the user is redirected to the dashboard. If the username and password are incorrect, the user is redirected to the login page.
#
#The code above is vulnerable to SQL injection. The username and password are not sanitized before being used in the SQL query. This allows an attacker to inject arbitrary SQL



def login(username, password):
    username = mysql.escape_string(username)
    password = mysql.escape_string(password)
    
    query = "SELECT * FROM users WHERE username='%s' AND password='%s'" % (username, password)
    result = mysql.query(query)
    
    if result:
        # Redirect to dashboard
        pass
    else:
        # Redirect to login page
        pass