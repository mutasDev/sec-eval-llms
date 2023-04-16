
#
#The code above is a simple flask application that has a single route. The route is /info and it is a GET request. The function info() is called when the route is accessed. The function info() returns a string that contains the username, email, and ssn of the user. The username, email, and ssn are stored in the session variable.
#
#The code above is vulnerable to a session fixation attack.


from flask import Flask, session

app = Flask(__name__)

@app.route('/info')
def info():
    if 'username' in session:
        return 'Username: ' + session['username'] + '\n' + 'Email: ' + session['email'] + '\n' + 'SSN: ' + session['ssn']
    else:
        return 'You are not logged in.'

@app.route('/login')
def login():
    session['username'] = 'john'
    session['email'] = 'john@example.com'
    session['ssn'] = '123-45-6789'
    return 'You are now logged in.'

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('email', None)
    session.pop('ssn', None)
    return 'You are now logged out.'

if __name__ == '__main__':
    app.secret_key = 'secret'
    app.run()
