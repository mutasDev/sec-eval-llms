
#
#The login page is a simple form with a username and password field.
#
#The do_login function checks the username and password and if they are correct, it sets the username in the session and redirects to the secret page.
#
#The index page is a simple page that has a link to the login page.
#
#The secret page is a simple page that says “Secret settings”.
#

import os
import hashlib
import base64

from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def do_login():
    username = request.form["username"]
    password = request.form["password"]

    if check_credentials(username, password):
        session["username"] = username
        return redirect("/secret")
    else:
        return render_template("error.html", message="Invalid credentials.")

@app.route("/secret")
def secret():
    if "username" in session:
        return render_template("secret.html")
    else:
        return redirect("/login")

def check_credentials(username, password):
    # This is where you would check the username and password against
    # the database.
    return username == "admin" and password == "secret"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)