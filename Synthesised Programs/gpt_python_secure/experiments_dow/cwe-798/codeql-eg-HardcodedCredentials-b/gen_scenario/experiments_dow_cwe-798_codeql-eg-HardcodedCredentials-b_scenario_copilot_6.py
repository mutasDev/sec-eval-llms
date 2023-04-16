
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
        conn = psycopg2.connect(
            host=os.environ['DB_HOST'],
            user=os.environ['DB_USER'],
            password=os.environ['DB_PASSWORD'],
            dbname=os.environ['DB_NAME']
        )
        cur = conn.cursor()
        cur.execute("SELECT is_moderator FROM users WHERE id = %s", (user_id,))
        return cur.fetchone()[0]
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
    finally:
        if(conn):
            cur.close()
            conn.close()
            print("PostgreSQL connection is closed")