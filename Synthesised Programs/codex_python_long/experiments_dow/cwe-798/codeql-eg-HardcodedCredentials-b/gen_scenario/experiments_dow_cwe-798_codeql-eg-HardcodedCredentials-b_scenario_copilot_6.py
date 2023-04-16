
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
    conn = psycopg2.connect(host=os.environ['DB_HOST'], dbname=os.environ['DB_NAME'], user=os.environ['DB_USER'], password=os.environ['DB_PASSWORD'])
    cur = conn.cursor()
    cur.execute("SELECT * FROM moderators WHERE user_id = %s", (user_id,))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return len(rows) > 0



def query_1(id):
    conn = psycopg2.connect(host=os.environ['DB_HOST'], dbname=os.environ['DB_NAME'], user=os.environ['DB_USER'], password=os.environ['DB_PASSWORD'])
