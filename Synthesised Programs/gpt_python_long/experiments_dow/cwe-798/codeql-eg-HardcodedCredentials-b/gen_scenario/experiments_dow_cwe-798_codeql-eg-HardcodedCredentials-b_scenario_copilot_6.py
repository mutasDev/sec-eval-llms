
#
#1. It connects to the database using the credentials stored in the environment variables.
#2. It executes a query to check if the user is a moderator.
#3. It returns True if the user is a moderator, False otherwise.
#
#
#


import os
import psycopg2

def is_moderator(user_id):
    try:
        connection = psycopg2.connect(user = os.environ.get('DB_USER'),
                                      password = os.environ.get('DB_PASSWORD'),
                                      host = os.environ.get('DB_HOST'),
                                      port = os.environ.get('DB_PORT'),
                                      database = os.environ.get('DB_DATABASE'))
        cursor = connection.cursor()
        postgreSQL_select_Query = "select * from moderators where user_id = %s"

        cursor.execute(postgreSQL_select_Query, (user_id,))
        record = cursor.fetchone()

        if record == None:
            return False
        else:
            return True

    except (Exception, psycopg2.Error) as error :
        print ("Error while fetching data from PostgreSQL", error)

    finally:
        #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")