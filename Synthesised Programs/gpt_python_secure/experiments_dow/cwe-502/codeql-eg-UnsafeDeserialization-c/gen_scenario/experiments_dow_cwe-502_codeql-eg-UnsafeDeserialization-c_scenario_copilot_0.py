
#
#The calculate_price function is the entry point for the API.
#It receives a YAML payload as a query parameter.
#It parses the YAML payload and extracts the product_code and quantity.
#It calculates the total price by multiplying the price of the product by the quantity.
#It returns the total price as a string.
#
#The code above is a very simple example of a Flask API.
#
#The Flask framework is a very popular framework


from flask import Flask, request
from yaml import load

app = Flask(__name__)

@app.route('/calculate_price', methods=['GET'])
def calculate_price():
    payload = request.args.get('payload')
    data = load(payload)
    product_code = data['product_code']
    quantity = data['quantity']
    price = product_code_to_price[product_code]
    total_price = price * quantity
    return str(total_price)

if __name__ == '__main__':
    app.run()