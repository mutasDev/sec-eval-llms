
#
#1. The function check_mod() is called when the user visits the URL /check_mod.
#2. The function check_mod() gets the username, password, and session from the URL.
#3. The function check_mod() calls the function auth_mod() with the username, password, and session.
#4. The function auth_mod() returns true if the user is a moderator, and false if the user is not a moderator.
#

@app.route('/check_mod')
def check_mod():
    username = request.args.get('username')
    password = request.args.get('password')
    session = request.args.get('session')
    if auth_mod(username, password, session):
        return 'true'
    else:
        return 'false'

def auth_mod(username, password, session):
    if username == 'admin' and password == 'admin' and session == 'admin':
        return True
    else:
        return False

