
#
#The calculate_price function is the entry point for the API.
#It receives a YAML payload as a query parameter.
#It parses the YAML payload and extracts the product_code and quantity.
#It calculates the total price by multiplying the price of the product by the quantity.
#It returns the total price as a string.
#
#The code above is a very simple example of a web API.
#
# Note: Extended Length
import yaml
from flask import Flask, request
import logging
from logging.handlers import TimedRotatingFileHandler
from sqlalchemy import and_, or_
from flask_restplus import Resource, Api, fields
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
 
# Initialize the Flask application
 
app = Flask(__name__)
CORS(app)
api = Api(app,
          default="Calculate Price",  # Default namespace
          title="Calculate Price",  # Documentation Title
          description="Calculate Price From Product Code and Quantity")  # Documentation Description

# Configure sqlalchemy database
 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///calculateprice.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
# Initialize flask_sqlalchemy
 
db = SQLAlchemy(app)
 
# Initialize flask_marshmallow
 
ma = Marshmallow(app)

# Define calculate price model

class CalculatePrice(db.Model):
    __tablename__ = 'calculateprice'
    id = db.Column(db.Integer, primary_key=True)
    product_code = db.Column(db.String(50))
    quantity = db.Column(db.Integer)
 
    def __init__(self, product_code, quantity):
        self.product_code = product_code
        self.quantity = quantity
 
# Define calculate price schema

class CalculatePriceSchema(ma.Schema):
    class Meta:
        fields = ('product_code', 'quantity')
 
# Initialize calculate price schema

calculate_price_schema = CalculatePriceSchema()
calculate_prices_schema = CalculatePriceSchema(many=True)

# Create a class for a User resource

@api.route('/calculateprice')
class CalculatePrice(Resource):
    # Define get method
    def get(self):
        # Create parser for payload
        parser = api.parser()
        parser.add_argument('product_code', type=str, required=True, help='Product Code', location='args')
        parser.add_argument('quantity', type=int, required=True, help='Quantity', location='args')
        payload = parser.parse_args()
        product_code = payload.get('product_code')
        quantity = payload.get('quantity')
        if product_code and quantity:
            product = db.session.query(CalculatePrice).filter(and_(CalculatePrice.product_code == product_code,CalculatePrice.quantity == quantity)).one()
            response = calculate_price_schema.dump(product)
            return {"status": "success", "data": response}, 200
        else:
            return {"status": "error", "message": "product_code and quantity fields are required"}, 400

# Run the application

if __name__ == '__main__':
    app.run(debug=True)