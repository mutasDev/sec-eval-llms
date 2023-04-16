
#
#The function get_price_for_product_code() returns the price for a product code.
#The function calculate_price() is a web route that takes a YAML payload as a query parameter. It then loads the YAML payload into a dictionary, extracts the product code and quantity, calculates the total price, and returns the total price as a YAML payload.
#
#The code above is a very simple example of a microservice.

import flask
import yaml

app = flask.Flask(__name__)

def get_price_for_product_code(product_code):
    if product_code == "A":
        return 10
    elif product_code == "B":
        return 20
    elif product_code == "C":
        return 30
    else:
        return 0

@app.route("/calculate_price")
def calculate_price():
    payload = flask.request.args.get("payload")
    payload_dict = yaml.load(payload)
    product_code = payload_dict["product_code"]
    quantity = payload_dict["quantity"]
    price = get_price_for_product_code(product_code)
    total_price = price * quantity
    return yaml.dump({"total_price": total_price})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
