
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
import pymongo
import psycopg2
import psycopg2.extras
import datetime
import requests

#Connect to the database
#conn = psycopg2.connect(
#  host="localhost",
#  database="sensor",
#  user="rohit",
#  password="rohit")
#cursor = conn.cursor()

#Connect to the database
#conn = pymongo.MongoClient(os.environ['MONGODB_URI'])
#dbs = conn.get_default_database()
#temperature = dbs.temperatures

#Function to get the temperature
def temperature_for_location(latitude, longitude, date):

    url = "http://localhost:3000/api/temperature_for_location"

    payload = {
        "latitude": latitude,
        "longitude": longitude,
        "date": date
    }

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        return response.json()
    else:
        return None