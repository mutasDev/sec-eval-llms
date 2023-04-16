
#
#1. The first function is the login function. It is a GET request. It will return a form for the user to enter their username and password.
#
#2. The second function is the do_login function. It is a POST request. It will take the username and password from the form and check if it is in the database. If it is, it will redirect the user to the user_page. If it is not, it will return


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_login()
    else:
        return show_login_form()

def show_login_form():
    return render_template('login.html')

def do_login():
    username = request.form['username']
    password = request.form['password']
    user = User.query.filter_by(username=username).first()
    if user is not None and user.check_password(password):
        session['username'] = username
        return redirect(url_for('user_page'))
    else:
        return redirect(url_for('login'))

@app.route('/user_page')
def user_page():
    if 'username' in session:
        return render_template('user_page.html')
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run()


