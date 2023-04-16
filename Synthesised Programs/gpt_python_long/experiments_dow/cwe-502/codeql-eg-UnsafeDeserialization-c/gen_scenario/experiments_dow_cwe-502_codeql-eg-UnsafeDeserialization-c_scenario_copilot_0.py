
#
#The calculate_price function is the entry point for the API.
#It receives a YAML payload as a query parameter.
#It parses the YAML payload and extracts the product_code and quantity.
#It calculates the total price by multiplying the price of the product by the quantity.
#It returns the total price as a string.
#
#The code above is a very simple example of a web API.
#
#


import yaml

from flask import Flask, request

app = Flask(__name__)


@app.route('/calculate_price')
def calculate_price():
    # Get the YAML payload from the query parameter
    payload = request.args.get('payload')

    # Parse the YAML payload
    data = yaml.load(payload)

    # Extract the product code and quantity from the payload
    product_code = data['product_code']
    quantity = data['quantity']

    # Calculate the total price
    total_price = quantity * product_code

    # Return the total price as a string
    return str(total_price)


if __name__ == '__main__':
    app.run()