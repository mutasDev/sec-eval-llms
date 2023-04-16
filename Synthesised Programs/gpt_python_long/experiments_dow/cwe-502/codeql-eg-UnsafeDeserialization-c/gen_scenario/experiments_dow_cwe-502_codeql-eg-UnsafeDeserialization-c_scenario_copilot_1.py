
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


from flask import Flask, request

app = Flask(__name__)

@app.route('/price', methods=['GET'])
def get_price():
    product_code = request.args.get('product_code')
    quantity = int(request.args.get('quantity'))
    price = 0
    if product_code == 'A':
        price = 5
    elif product_code == 'B':
        price = 10
    elif product_code == 'C':
        price = 15
    elif product_code == 'D':
        price = 20
    else:
        price = 0
    return str(price * quantity)

if __name__ == '__main__':
    app.run(port=5000)