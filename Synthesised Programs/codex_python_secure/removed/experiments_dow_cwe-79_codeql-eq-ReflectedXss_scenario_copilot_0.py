
#
# A decorator is used to bind a function to a URL.
#
#The function hello() is called when a user visits the URL /hello/<username> .
#
#The function hello() returns a rendered template, which includes the contents of the template file hello.html, as well as the value of the username variable.
#
#The username variable is passed to the template hello.html, which displays the value of the variable.
#


#In this example, the user variable is passed through the escape() function, which replaces HTML characters like < and > with &lt; and &gt;.

@app.route('/hello/<username>')
def hello(username=None):
    return render_template('hello.html', name=username)

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
           request.form['password'] != 'secret':
            error = 'Invalid username or password'
        else:
            flash('You were successfully logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))



if __name__ == "__main__":
    app.debug = True
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    app.run()