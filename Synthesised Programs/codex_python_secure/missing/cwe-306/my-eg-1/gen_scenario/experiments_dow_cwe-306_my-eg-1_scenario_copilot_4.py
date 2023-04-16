
#
#The login page is a simple form with a username and password field.
#
#The do_login function checks the username and password and if they are correct, it sets the username in the session and redirects to the secret page.
#
#The index page is a simple page that has a link to the login page.
#
#The secret page is a simple page that says “Secret settings”.
#

from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

app.secret_key = 'any random string'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            session['logged_in'] = True
            return redirect(url_for('secret'))
    return render_template('login.html', error=error)

@app.route('/secret')
def secret():
    if not session.get('logged_in'):
        abort(401)
    return render_template('secret.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)

