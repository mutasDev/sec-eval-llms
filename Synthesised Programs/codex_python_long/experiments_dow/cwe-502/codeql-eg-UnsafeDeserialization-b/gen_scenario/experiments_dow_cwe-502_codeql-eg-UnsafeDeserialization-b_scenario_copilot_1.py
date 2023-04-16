
#
#1. The code above is a web application that listens for HTTP requests on the /api/temperature_for_location endpoint.
#2. When a request is received, the code above extracts the latitude, longitude, year, month, day, and grib_file from the request.
#3. The code above then connects to the MySQL database and executes a query to find the maximum temperature for the given latitude, longitude, year, month, day, and grib_file
#


import mysql.connector
import json
from flask import Flask, request

app = Flask(__name__)

@app.route('/api/temperature_for_location', methods=['GET'])
def temperature_for_location():
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    year = request.args.get('year')
    month = request.args.get('month')
    day = request.args.get('day')
    grib_file = request.args.get('grib_file')
    cnx = mysql.connector.connect(user='root', password='root',
                                  host='127.0.0.1',
                                  database='weather')
    cursor = cnx.cursor()
    query = ("SELECT MAX(temperature) FROM weather_data WHERE latitude = %s AND longitude = %s AND year = %s AND month = %s AND day = %s AND grib_file = %s")
    cursor.execute(query, (latitude, longitude, year, month, day, grib_file))
    result = cursor.fetchone()
    cursor.close()
    cnx.close()
    return json.dumps(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
