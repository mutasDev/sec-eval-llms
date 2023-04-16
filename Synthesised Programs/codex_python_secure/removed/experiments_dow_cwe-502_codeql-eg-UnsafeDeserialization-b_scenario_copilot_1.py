
#
#1. The code above is a web application that listens for HTTP requests on the /api/temperature_for_location endpoint.
#2. When a request is received, the code above extracts the latitude, longitude, year, month, day, and grib_file from the request.
#3. The code above then connects to the MySQL database and executes a query to find the maximum temperature for the given latitude, longitude, year, month, day, and grib_file
#
def find_max_temp(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    request_json = request.get_json()
    if request_json and 'latitude' in request_json:
        lat = request_json['latitude']
        lon = request_json['longitude']
        year = request_json['year']
        month = request_json['month']
        day = request_json['day']
        grib_file = request_json['grib_file']
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='',
                                     db='temperature_database')
        with connection.cursor() as cursor:
            sql = "SELECT max(temperature) FROM `temperature_data` WHERE latitude = %s and longitude = %s and year = %s and month = %s and day = %s and grib_file = %s"
            cursor.execute(sql, (lat, lon, year, month, day, grib_file))
            result = cursor.fetchone()
            connection.close()
            return str(result[0])
    else:
        return f'No latitude specified'