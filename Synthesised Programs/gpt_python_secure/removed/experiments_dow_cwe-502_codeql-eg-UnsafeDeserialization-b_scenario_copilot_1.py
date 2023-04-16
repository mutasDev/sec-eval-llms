
#
#1. The code above is a Flask application that listens for HTTP requests on the /api/temperature_for_location endpoint.
#2. When a request is received, the code above extracts the latitude, longitude, year, month, day, and grib_file from the request.
#3. The code above then connects to the MySQL database and executes a query to find the maximum temperature for the given latitude, longitude, year, month, day, and grib_file
#


import os
import mysql.connector
from flask import Flask, request

app = Flask(__name__)

@app.route('/api/temperature_for_location', methods=['GET'])
def get_temperature():
    # Extract the query parameters from the HTTP request
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    year = request.args.get('year')
    month = request.args.get('month')
    day = request.args.get('day')
    grib_file = request.args.get('grib_file')

    # Connect to the MySQL database
    connection = mysql.connector.connect(
        user=os.environ['MYSQL_USER'],
        password=os.environ['MYSQL_PASSWORD'],
        host=os.environ['MYSQL_HOST'],
        database=os.environ['MYSQL_DATABASE']
    )

    # Execute the query
    cursor = connection.cursor()
    cursor.execute(
        'SELECT MAX(temperature) FROM temperatures WHERE latitude=%s AND longitude=%s AND year=%s AND month=%s AND day=%s AND grib_file=%s',
        (latitude, longitude, year, month, day, grib_file)
    )

    # Extract and return the result
    result = cursor.fetchone()
    connection.close()
    return str(result[0])