
#
#The code above is a simple registration form that takes in a username and password. The password is then hashed using the pbkdf2_hmac algorithm. The salt is generated using the os.urandom function. The salt is then concatenated with the hashed password and stored in the database.
#
#NOTE: Extended length


# The code below is the login form.

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('dashboard'))
            else:
                flash('Invalid username/password combination')
                return redirect(url_for('login'))
        else:
            flash('Invalid username/password combination')
            return redirect(url_for('login'))
    return render_template('login.html')

""" 
The code above is the login form. The username and password are taken from the form and the user is queried from the database. The password is then checked using the check_password_hash function. If the password is correct, the user is logged in using the login_user function.
"""

# The code below is the dashboard.

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', name=current_user.name)

""" 
The code above is the dashboard. The login_required decorator is used to ensure that only logged in users can access the dashboard. The current_user variable is used to get the name of the logged in user.
"""

# The code below is the logout function.

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

""" 
The code above is the logout function. The login_required decorator is used to ensure that only logged in users can logout. The logout_user function is used to logout the user.
"""

# The code below is the main function.

if __name__ == '__main__':
    app.run(debug=True)

""" 
The code above is the main function. The debug=True argument is used to enable the debug mode.
"""