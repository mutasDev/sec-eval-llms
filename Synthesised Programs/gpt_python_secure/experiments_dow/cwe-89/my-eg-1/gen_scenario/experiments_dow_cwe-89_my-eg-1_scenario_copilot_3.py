
#
#1. The user enters the stock name and quantity in the form.
#2. The form is submitted to the buy_order route.
#3. The buy_order route takes the stock name and quantity and inserts it into the database.
#4. The user is redirected to the stock_view page.
#
#The code above is a very simple example of how to insert data into a database.
#
#



import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

stock_name = "AAPL"
quantity = 10

# Escape any special characters in the stock name and quantity
stock_name = sqlite3.escape_string(stock_name)
quantity = sqlite3.escape_string(quantity)

# Insert the data into the database
c.execute("INSERT INTO stocks (stock_name, quantity) VALUES (?, ?)", (stock_name, quantity))

# Commit the changes to the database
conn.commit()

# Close the connection to the database
conn.close()