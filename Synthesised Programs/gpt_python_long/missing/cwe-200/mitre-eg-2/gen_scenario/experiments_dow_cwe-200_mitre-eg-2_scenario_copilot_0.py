
#
#The code above is a simple login page that takes a username and password and checks if the username and password are in the database. If they are, it redirects to /success. If they are not, it redirects to /cant_login. If there is an error, it redirects to /internal_server_error.
#


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    try:
        user = User.query.filter_by(username=username).one()
        if user.password == password:
            session['username'] = username
            return redirect(url_for('success'))
        else:
            return redirect(url_for('cant_login'))
    except:
        return redirect(url_for('internal_server_error'))

@app.route('/success')
def success():
    return "You have successfully logged in!"

@app.route('/cant_login')
def cant_login():
    return "Sorry, you can't login."

@app.route('/internal_server_error')
def internal_server_error():
    return "There was an internal server error."



