
#
#1. The first function is the login function. It is a GET request.
#2. The second function is the do_login function. It is a POST request.
#3. The third function is the index function. It is a GET request.
#4. The fourth function is the user_page function. It is a GET request.
#5. The fifth function is the admin_page function. It is a GET request.



@app.route('/login', methods=['GET'])
def login():
    """
    This function is the login function. It is a GET request.
    """
    return render_template('login.html')

@app.route('/do_login', methods=['POST'])
def do_login():
    """
    This function is the do_login function. It is a POST request.
    """
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == 'admin':
        session['username'] = username
        session['password'] = password
        return redirect(url_for('admin_page'))
    elif username == 'user' and password == 'user':
        session['username'] = username
        session['password'] = password
        return redirect(url_for('user_page'))
    else:
        return redirect(url_for('login'))

@app.route('/index', methods=['GET'])
def index():
    """
    This function is the index function. It is a GET request.
    """
    return render_template('index.html')



















































































































































