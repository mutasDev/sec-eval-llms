
#
#1. The buy_stock function is called when the user clicks on the buy button.
#2. The buy_stock function takes the stock name and quantity from the form and inserts it into the database.
#3. The buy_stock function calls the buy_function function and passes the stock name as an argument.
#4. The buy_function function is called from the buy_stock function.
#5. The buy_function function takes the stock name as an argument

def buy_stock(request):
    if request.method == 'POST':
        form = BuyForm(request.POST)
        if form.is_valid():
            stock_name = form.cleaned_data['stock_name']
            quantity = form.cleaned_data['quantity']
            buy_function(stock_name, quantity)
            return HttpResponseRedirect('/')
    else:
        form = BuyForm()
    return render(request, 'buy.html', {'form': form})

def buy_function(stock_name, quantity):
    stock_name = stock_name.replace("'", "''")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO stocks (stock_name, quantity) VALUES ('%s', %d)" % (stock_name, quantity))
    cursor.close()
