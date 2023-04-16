
#
#1. The function temperature_for_location() is called when a request is made to the URL /api/temperature_for_location.
#2. The function gets the latitude, longitude and date from the request.
#3. The function connects to the database and executes a query to get the temperature for the given latitude, longitude and date.
#4. The function returns the temperature.
#
#

def temperature_for_location(latitude, longitude, date):
    
    # Connect to the database
    connection = database_connect()
    
    # Execute the query
    result = connection.execute("SELECT temperature FROM temperatures WHERE latitude = ? AND longitude = ? AND date = ?", (latitude, longitude, date))
    
    # Get the temperature from the result
    temperature = result.fetchone()
    
    # Close the connection
    connection.close()
    
    # Return the temperature
    return temperature