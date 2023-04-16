
#
#1. The first function is the login function. It is a GET request.
#2. The second function is the do_login function. It is a POST request.
#3. The third function is the index function. It is a GET request.
#4. The fourth function is the user_page function. It is a GET request.
#5. The fifth function is the admin_page function. It is a GET request.

def login(request):
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if check_login(username, password):
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error="Invalid username or password")

def do_login(request):
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if check_login(username, password):
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error="Invalid username or password")

def index(request):
    if request.method == 'GET':
        return render_template('index.html')

def user_page(request):
    if request.method == 'GET':
        return render_template('user_page.html')

def admin_page(request):
    if request.method == 'GET':
        return render_template('admin_page.html')