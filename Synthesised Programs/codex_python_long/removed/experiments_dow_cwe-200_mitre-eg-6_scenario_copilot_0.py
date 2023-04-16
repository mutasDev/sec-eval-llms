
#
#The code above is a simple web application that has a single route. The route is /info and it is a GET request. The function info() is called when the route is accessed. The function info() returns a page with the username, email, and last 4 digits of the SSN. The username, email, and SSN are stored in the session variable.
#
#The code above is vulnerable to a session fixation attack.
#


from flask import Flask, session, redirect, url_for, escape, request

app = Flask(__name__)

@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return 'Logged in as ' + username + '<br>' + \
        "<b><a href = '/logout'>click here to log out</a></b>"
    return "You are not logged in <br><a href = '/login'></b>" + \
        "click here to log in</b></a>"

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form action = "" method = "post">
            <p><input type = text name = username/></p>
            <p><input type = submit value = Login/></p>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it is there
    session.pop('username', None)
    return redirect(url_for('index'))

# set the secret key. keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == "__main__":
    app.run(debug = True)