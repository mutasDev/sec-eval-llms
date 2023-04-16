
#
#1. The code above is a web application that listens for HTTP requests on the /api/temperature_for_location endpoint.
#2. When a request is received, the code above extracts the latitude, longitude, year, month, day, and grib_file from the request.
#3. The code above then connects to the MySQL database and executes a query to find the maximum temperature for the given latitude, longitude, year, month, day, and grib_file
#

#Note: Extended Length


@app.route('/api/temperature_for_location', methods=['GET'])
def get_temperature():
    """
    This is the endpoint that responds to GET requests.
    """
    try:
        # Extract the parameters from the request
        latitude = float(request.args.get('latitude'))
        longitude = float(request.args.get('longitude'))
        year = int(request.args.get('year'))
        month = int(request.args.get('month'))
        day = int(request.args.get('day'))
        grib_file = request.args.get('grib_file')
    except ValueError as e:
        # Return an error response if any of the parameters are invalid
        return jsonify({'error': str(e)}), 400

    try:
        # Connect to the MySQL database
        cursor = mysql.connect().cursor()
    except Exception as e:
        # Return an error response if the database can't be reached
        return jsonify({'error': str(e)}), 500

    try:
        # Execute a SQL query to find the maximum temperature for the given latitude, longitude, year, month, day, and grib_file
        cursor.execute("""
            SELECT MAX(temperature) FROM grib_data WHERE 
            latitude = %s AND 
            longitude = %s AND 
            year = %s AND 
            month = %s AND 
            day = %s AND 
            grib_file = %s
        """, (latitude, longitude, year, month, day, grib_file))
        result = cursor.fetchone()
        cursor.close()
    except Exception as e:
        # Return an error response if the query fails
        return jsonify({'error': str(e)}), 500

    # Return the maximum temperature
    return jsonify({'max_temperature': result[0]})


if __name__ == '__main__':
    app.run()

@app.route('/', methods=['GET'])
def index():
    # Connect to the database
    connection = mysql.connect()
    # Get the cursor, which is used to execute queries
    cursor = connection.cursor()
    # Select the index from the database
    cursor.execute("SELECT * FROM index")
    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()
    return render_template('index.html', results=results)

@app.route('/add', methods=['POST'])
def add():
    try:
        # Connect to the database
        connection = mysql.connect()
        # Get the cursor, which is used to execute queries
        cursor = connection.cursor()
        # Insert new record
        cursor.execute("INSERT INTO index (author, title, isbn) VALUES (%s, %s, %s)", (request.form['author'], request.form['title'], request.form['isbn']))
        connection.commit()
    except Exception as e:
        return(str(e))
    finally:
        return redirect("/")

@app.route('/edit/<id>', methods=['POST'])
def edit(id):
    try:
        # Connect to the database
        connection = mysql.connect()
        # Get the cursor, which is used to execute queries
        cursor = connection.cursor()
        # Edit record
        cursor.execute("UPDATE index SET author = %s, title = %s, isbn = %s WHERE id = %s", (request.form['author'], request.form['title'], request.form['isbn'], id))
        connection.commit()
    except Exception as e:
        return(str(e))
    finally:
        return redirect("/")

@app.route('/delete/<string:id>', methods=['GET'])
def delete(id):
    try:
        # Connect to the database
        connection = mysql.connect()
        # Get the cursor, which is used to execute queries
        cursor = connection.cursor()
        # Edit record
        cursor.execute("DELETE FROM index WHERE id = %s", id)
        connection.commit()
    except Exception as e:
        return(str(e))
    finally:
        return redirect("/")

@app.route('/search', methods=['GET'])
def search():
    try:
        # Connect to the database
        connection = mysql.connect()
        # Get the cursor, which is used to execute queries
        cursor = connection.cursor()
        # Get search query
        query = request.args.get('query')
        # Execute a SQL query to find the author, title, and isbn of the book with the given query
        cursor.execute("""
            SELECT author, title, isbn FROM index WHERE 
            author LIKE %s OR 
            title LIKE %s OR 
            isbn LIKE %s
        """, (query + '%', query + '%', query + '%'))
        # Fetch all the rows in a list of lists.
        results = cursor.fetchall()
        return render_template('search_results.html', results=results)
    except Exception as e:
        return(str(e))
    finally:
        return redirect("/")