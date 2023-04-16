
#
#1. I have a login.html page which has a form with username and password fields.
#2. I have a login file which has a login function which takes the username and password from the form and checks if the username and password exists in the database.
#3. If the username and password exists in the database, then the user is redirected to the home page.
#4. If the username and password does not exist in the database, then the user is redirected to the login page.



from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)

# Configure db
db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form
        username = userDetails['username']
        password = userDetails['password']
        cur = mysql.connection.cursor()
        cur.execute("SELECT * from users where username=%s and password=%s", (username, password))
        user = cur.fetchone()
        if user:
            return redirect(url_for('home'))
        else:
            return 'Invalid username/password combination'
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
