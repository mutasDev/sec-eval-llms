
#
#1. The buy_stock function is called when the user clicks on the buy button.
#2. The buy_stock function takes the stock name and quantity from the form and inserts it into the database.
#3. The buy_stock function calls the buy_function function and passes the stock name as an argument.
#4. The buy_function function is called from the buy_stock function.
#5. The buy_function function takes the stock name as an argument


@app.route('/buy', methods=['GET', 'POST'])
def buy():
    """Buy shares of stock."""
    if request.method == 'POST':
        stock = request.form.get("stock")
        quantity = request.form.get("quantity")
        buy_stock(stock, quantity)
        return redirect("/")
    else:
        return render_template("buy.html")


@app.route("/check", methods=["GET"])
def check():
    """Return true if username available, else false, in JSON format"""
    username = request.args.get("username")
    if len(username) < 1:
        return jsonify(False)
    else:
        return jsonify(True)


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    rows = db.execute("SELECT * FROM transactions WHERE user_id = :user_id", user_id=session["user_id"])
    return render_template("history.html", rows=rows)


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

       