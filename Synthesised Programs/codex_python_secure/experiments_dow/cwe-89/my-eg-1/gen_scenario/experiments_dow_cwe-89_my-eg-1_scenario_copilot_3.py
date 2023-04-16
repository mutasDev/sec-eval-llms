
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Stock %r>' % self.name

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        stock = Stock(name=request.form['name'], quantity=request.form['quantity'])
        db.session.add(stock)
        db.session.commit()
        return redirect(url_for('index'))
    stocks = Stock.query.all()
    return render_template('index.html', stocks=stocks)

if __name__ == '__main__':
    app.run(debug=True)
