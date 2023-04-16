
#
#1. The first function is the login function. It is a GET request.
#2. The second function is the do_login function. It is a POST request.
#3. The third function is the index function. It is a GET request.
#4. The fourth function is the user_page function. It is a GET request.
#5. The fifth function is the admin_page function. It is a GET request.



@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def do_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return index()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/user")
def user_page():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "Hello Boss!"


@app.route("/admin")
def admin_page():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "Hello Admin!"


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True, host='0.0.0.0', port=4000)



