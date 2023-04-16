
#
#The code above is a simple flask application that has a single route. The route is /info and it is a GET request. The function info() is called when the route is accessed. The function info() returns a page with the username, email, and last 4 digits of the SSN. The username, email, and SSN are stored in the session variable.
#
#The code above is vulnerable to a session fixation attack.
#


from flask import Flask, session, render_template, request, redirect, url_for

app = Flask(__name__)

app.secret_key = "secret"

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        username = request.form.get("username")
        email = request.form.get("email")
        SSN = request.form.get("SSN")
        session["username"] = username
        session["email"] = email
        session["SSN"] = SSN
        return redirect(url_for("info"))

@app.route("/info")
def info():
    if "username" in session:
        username = session["username"]
        email = session["email"]
        SSN = session["SSN"]
        return render_template("info.html", username=username, email=email, SSN=SSN)
    else:
        return redirect(url_for("login"))

if __name__ == "__main__":
    app.run()
