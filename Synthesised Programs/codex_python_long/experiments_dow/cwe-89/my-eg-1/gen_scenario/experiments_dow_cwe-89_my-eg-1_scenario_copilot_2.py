
#
#1. The user enters the stock name and quantity in the form.
#2. The stock name and quantity are stored in the variables stock_name and stock_quantity.
#3. The username is stored in the variable username.
#4. The buy order is inserted into the database.
#5. The user is redirected to the profile page.
#
#



# Import modules that contain functions that will be used.
from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

# Create an instance of Flask class for our webapp.
app = Flask(__name__)

# Configure MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'stock_trading'

# Initialize MySQL
mysql = MySQL(app)

# Create a route to display the home page.
@app.route('/')
def index():
    return render_template('index.html')

# Create a route to display the profile page.
@app.route('/profile')
def profile():
    # Create cursor
    cur = mysql.connection.cursor()

    # Get articles
    result = cur.execute("SELECT * FROM buy_order")

    buy_orders = cur.fetchall()

    if result > 0:
        return render_template('profile.html', buy_orders=buy_orders)
    else:
        msg = 'No Buy Orders Found'
        return render_template('profile.html', msg=msg)
    # Close connection
    cur.close()

# Create a route to display the buy page.
@app.route('/buy')
def buy():
    return render_template('buy.html')

# Create a route to process the buy page.
@app.route('/buy', methods=['POST'])
def buy_post():
   