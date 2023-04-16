
#
#1. The first function is the login function. It is a GET request.
#2. The second function is the do_login function. It is a POST request.
#3. The third function is the index function. It is a GET request.
#4. The fourth function is the user_page function. It is a GET request.
#5. The fifth function is the admin_page function. It is a GET request.
@app.route('/login', methods=['GET'])
def login():
    #Provides the login form to the user
    return render_template('login.html', error=request.args.get('error'))
    #If an error is present, the error message will be displayed in the login form

@app.route('/do_login', methods=['POST'])
def do_login():
    #This function checks to see if the user is in the database
    user=db_session.query(User).filter_by(username=request.form['username']).first()
    if user is None:
        #If the user is not in the database, the user will be redirected to the login page with an error message
        return redirect(url_for('login', error="That username is not registered"))
    else:
        hashed_password=user.password
        #This is where the database password is stored
        salt=user.salt
        #This is where the database salt is stored
        input_password=request.form['password']
        #This is where the user's password is stored
        hashed_input=hashlib.sha512(input_password + salt).hexdigest()
        #This hashes the user's password
        if hashed_input == hashed_password:
            #If the hashed password matches the one in the database, the user will be logged in and redirected to the index page
            session['username']=request.form['username']
            return redirect(url_for('index'))
        else:
            #If the hashed password does not match the one in the database, the user will be redirected to the login page with an error message
            return redirect(url_for('login', error="That password is incorrect"))

@app.route('/logout', methods=['GET'])
def logout():
    #This function logs the user out and redirected to the login page
    del session['username']
    return redirect(url_for('login'))


@app.route('/')
def index():
    #If the user is not logged in, they will be redirected to the login page
    if 'username' not in session:
        return redirect(url_for('login'))
    else:
        #If the user is logged in, they will be redirected to the index page
        return redirect(url_for('user_page'))

@app.route('/user_page', methods=['GET'])
def user_page():
    #If the user is not logged in, they will be redirected to the login page
    if 'username' not in session:
        return redirect(url_for('login'))
    else:
        #If the user is logged in, they will be redirected to the user_page
        return render_template('user_page.html')

@app.route('/admin_page', methods=['GET'])
def admin_page():
    #If the user is not logged in, they will be redirected to the login page
    if 'username' not in session:
        return redirect(url_for('login'))
    else:
        #If the user is logged in and the user is an administrator, they will be redirected to the admin_page
        user=db_session.query(User).filter_by(username=session['username']).first()
        if user.is_admin:
            return render_template('admin_page.html')
        else:
            #If the user is logged in, but the user is not an administrator, the user will be redirected to the user_page
            return redirect(url_for('user_page'))