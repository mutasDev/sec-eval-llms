
#
#The code above is a simple login page that takes a username and password and checks if the username and password are in the database. If they are, it redirects to /success. If they are not, it redirects to /cant_login. If there is an error, it redirects to /internal_server_error.
#

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    try:
        if db.check_login(username, password):
            return redirect('/success')
        else:
            return redirect('/cant_login')
    except Exception as e:
        return redirect('/internal_server_error')