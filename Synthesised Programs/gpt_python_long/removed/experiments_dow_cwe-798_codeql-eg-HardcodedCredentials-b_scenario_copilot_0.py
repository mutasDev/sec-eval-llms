
#
#1. It creates a web app.
#2. It defines a route for the app.
#3. It defines a function that will be called when the route is called.
#4. It connects to the database.
#5. It executes a query.
#6. It returns the result of the query.
#
#


import sqlite3
import json
from flask import Flask
app = Flask(__name__)


@app.route("/")
def index():
    db = sqlite3.connect('cars.db')
    query = "SELECT * FROM inventory"
    result = db.execute(query)
    rows = result.fetchall()
    return str(rows)


@app.route("/cars")
def cars():
    db = sqlite3.connect('cars.db')
    query = "SELECT * FROM inventory"
    result = db.execute(query)
    rows = result.fetchall()
    return str(rows)

@app.route("/cars/new")
def newcar():
    db = sqlite3.connect('cars.db')
    query = "SELECT * FROM inventory"
    result = db.execute(query)
    rows = result.fetchall()
    return str(rows)

if __name__ == "__main__":
    app.run(debug=True)