
#
#1. It connects to the database
#2. It executes a query to check if the username exists in the database
#3. If the username exists, it returns true, otherwise it returns false
#

def check_username_exists(username):
    # Connect to the database
    connection = connect_to_database()

    # Query the database
    query = "SELECT * FROM users WHERE username = '{}'".format(username)
    result = connection.execute(query)

    # Check if the username exists
    if result:
        return True
    else:
        return False

