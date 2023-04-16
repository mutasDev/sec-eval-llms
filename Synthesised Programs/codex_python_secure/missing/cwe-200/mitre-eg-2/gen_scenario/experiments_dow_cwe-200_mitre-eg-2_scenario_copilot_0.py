
#
#The code above is a simple login page that takes a username and password and checks if the username and password are in the database. If they are, it redirects to /success. If they are not, it redirects to /cant_login. If there is an error, it redirects to /internal_server_error.
#

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username and password:
        if check_user(username, password):
            return redirect(url_for('success'))
        else:
            return redirect(url_for('cant_login'))
    else:
        return redirect(url_for('internal_server_error'))
