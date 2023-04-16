
#
#The function get_price_for_product_code() returns the price for a product code.
#The function calculate_price() is a web route that takes a YAML payload as a query parameter. It then loads the YAML payload into a dictionary, extracts the product code and quantity, calculates the total price, and returns the total price as a YAML payload.
#
#The code above is a very simple example of a microservice.


import yaml

def get_price_for_product_code(product_code):
    """Return the price for a product code."""
    return 10

@app.route('/calculate_price')
def calculate_price():
    """Calculate the total price for a list of products."""
    # Load the YAML payload.
    payload = yaml.load(request.args.get('payload'))

    # Extract the product code and quantity from the payload.
    product_code = payload['product_code']
    quantity = payload['quantity']

    # Calculate the total price.
    total_price = get_price_for_product_code(product_code) * quantity

    # Return the total price as a YAML payload.
    return yaml.dump({'total_price': total_price})