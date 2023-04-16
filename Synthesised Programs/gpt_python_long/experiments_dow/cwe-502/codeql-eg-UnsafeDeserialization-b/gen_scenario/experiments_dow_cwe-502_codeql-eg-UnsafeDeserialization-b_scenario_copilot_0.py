
#
#1. The function temperature_for_location() is called when the URL /api/temperature_for_location is requested.
#2. The function gets the latitude, longitude and date from the payload.
#3. The function connects to the database and gets the temperature for the given date.
#4. The function returns the temperature.
#
#The code above is a simple example of how to use the database.
#
#The database is called Sensor


import os
import json
import psycopg2
from flask import Flask, request

app = Flask(__name__)

DATABASE_URL = os.environ['DATABASE_URL']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')

@app.route('/api/temperature_for_location', methods=['POST'])
def temperature_for_location():
    # Get the payload
    payload = request.get_json()

    # Get the latitude, longitude and date from the payload
    latitude = payload['latitude']
    longitude = payload['longitude']
    date = payload['date']

    # Connect to the database
    cur = conn.cursor()

    # Get the temperature for the given date
    cur.execute("SELECT temperature FROM sensor WHERE latitude = %s AND longitude = %s AND date = %s", (latitude, longitude, date))
    row = cur.fetchone()
    temperature = row[0]

    # Return the temperature
    return json.dumps({'temperature': temperature})

if __name__ == '__main__':
    app.run()