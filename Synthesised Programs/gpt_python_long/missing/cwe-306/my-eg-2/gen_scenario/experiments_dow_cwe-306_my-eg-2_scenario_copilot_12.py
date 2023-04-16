
#
#1. The user is redirected to the login page if he/she is not logged in.
#2. The user is redirected to the user page if he/she is logged in.
#3. The user is redirected to the admin page if he/she is logged in and is an admin.
#


def login_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if not session.get("user_id"):
            return redirect("/login")
        return func(*args, **kwargs)
    return decorated_function

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return render_template("error.html", message="must provide username")

        # Ensure password was submitted
        elif not request.form.get("password"):
            return render_template("error.html", message="must provide password")

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return render_template("error.html", message="invalid username and/or password")

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

   