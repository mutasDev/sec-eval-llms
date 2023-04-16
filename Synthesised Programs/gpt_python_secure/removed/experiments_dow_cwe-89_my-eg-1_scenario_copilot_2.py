
#
#1. The user enters the stock name and quantity in the form.
#2. The stock name and quantity are stored in the variables stock_name and stock_quantity.
#3. The username is stored in the variable username.
#4. The buy order is inserted into the database.
#5. The user is redirected to the profile page.
#
#
def buy_stock(request):
    stock_name = request.POST['stock_name']
    stock_quantity = request.POST['stock_quantity']
    username = request.POST['username']
    cursor = connection.cursor()
    cursor.execute("INSERT INTO buy_orders (stock_name, stock_quantity, username) VALUES (%s, %s, %s)", [stock_name, stock_quantity, username])
    return redirect('/profile/')