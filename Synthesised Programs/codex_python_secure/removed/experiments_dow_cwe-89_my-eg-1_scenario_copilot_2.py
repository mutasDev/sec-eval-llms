
#
#1. The user enters the stock name and quantity in the form.
#2. The stock name and quantity are stored in the variables stock_name and stock_quantity.
#3. The username is stored in the variable username.
#4. The buy order is inserted into the database.
#5. The user is redirected to the profile page.
#
#

#Stock Name and Quantity
stock_name = ''
stock_quantity = ''

#Username
username = ''

#Buy Order
order = ''

#SQL Query
query = """INSERT INTO orders (username, stock_name, stock_quantity) VALUES ('%s', '%s', '%s');""" % (username, stock_name, stock_quantity)

#Execute SQL Query
cursor.execute(query)

#Commit Changes to Database
db.commit()

#Redirect to Profile Page
redirect('/profile')