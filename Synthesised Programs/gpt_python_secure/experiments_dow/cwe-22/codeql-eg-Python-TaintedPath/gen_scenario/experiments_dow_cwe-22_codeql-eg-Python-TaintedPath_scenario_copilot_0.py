
#
#The @app.route('/img') decorator above the img() function associates the URL of /img with this function.
#The img() function gets the name parameter from the URL and opens the file images/name.
#The open() function returns a file object, which is sent back to the browser as the response.
#
#"""
#
#



import ssl
from flask import Flask, request, redirect, url_for, render_template, flash

app = Flask(__name__)
app.secret_key = 'some_secret'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                request.form['password'] != 'secret':
            error = 'Invalid credentials'
        else:
            flash('You were successfully logged in')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    flash('You were successfully logged out')
    return redirect(url_for('index'))

@app.route('/img')
def img():
    name = request.args.get('name')
    return open('images/' + name).read()

if __name__ == '__main__':
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.load_cert_chain('server.crt', 'server.key')
    app.run(host='0.0.0.0', port=8443, debug=True, ssl_context=context)