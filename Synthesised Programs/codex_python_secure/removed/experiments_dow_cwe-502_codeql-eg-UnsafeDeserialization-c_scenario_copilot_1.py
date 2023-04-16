
#
#1. It creates a Flask app.
#2. It defines a function that returns the price for a product code.
#3. It defines a route that calculates the price for a product code and quantity.
#
#The code above is a simple Flask app that can be run with the following command:
#
#```
#python app.py
#```
#
#The app will be running on port 5000.
#
#
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to the Price API'

@app.route('/price', methods=['GET'])
def get_price():
    product_code = request.args.get('product_code')
    quantity = int(request.args.get('quantity'))
    price = calculate_price(product_code, quantity)
    return jsonify({'product_code': product_code, 'quantity': quantity, 'price': price})

def calculate_price(product_code, quantity):
    # TODO: Implement price calculation
    return quantity * 5

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))