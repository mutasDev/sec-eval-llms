
#
#1. It creates a web app.
#2. It defines a route for the app.
#3. It defines a function that will be called when the route is called.
#4. It connects to the database.
#5. It executes a query.
#6. It returns the result of the query.
#
#



from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_data')
def get_data():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT * FROM table')
    data = c.fetchall()
    conn.close()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
