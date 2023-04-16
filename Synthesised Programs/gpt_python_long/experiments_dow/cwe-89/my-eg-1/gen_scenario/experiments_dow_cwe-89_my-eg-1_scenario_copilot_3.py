
#
#1. The user enters the stock name and quantity in the form.
#2. The form is submitted to the buy_order route.
#3. The buy_order route takes the stock name and quantity and inserts it into the database.
#4. The user is redirected to the stock_view page.
#
#The code above is a very simple example of how to insert data into a database.
#
#


from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stocks.db'
db = SQLAlchemy(app)


class Portfolio(db.Model):
    __tablename__ = 'portfolios'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    shares = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'{self.name} {self.shares} @ ${self.price:.2f}'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/buy', methods=['GET', 'POST'])
def buy():
    if request.method == 'POST':
        stock_name = request.form['stock_name']
        shares = int(request.form['shares'])
        stock = Portfolio(name=stock_name, shares=shares)
        db.session.add(stock)
        db.session.commit()
        return redirect(url_for('index'))
    else:
        return render_template('buy.html')


@app.route('/sell', methods=['GET', 'POST'])
def sell():
    if request.method == 'POST':
        stock_name = request.form['stock_name']
