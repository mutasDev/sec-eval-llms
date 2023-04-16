
#
#The login page is a simple form with a username and password field.
#
#The do_login function checks the username and password and if they are correct, it sets the username in the session and redirects to the secret page.
#
#The index page is a simple page that has a link to the login page.
#
#The secret page is a simple page that says “Secret settings”.
#
from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'any random string'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/secret')
def secret():
    if 'username' in session:
        return render_template('secret.html')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)