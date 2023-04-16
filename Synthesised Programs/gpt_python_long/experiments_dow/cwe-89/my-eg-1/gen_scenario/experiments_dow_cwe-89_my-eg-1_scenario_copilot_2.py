
#
#1. The user enters the stock name and quantity in the form.
#2. The stock name and quantity are stored in the variables stock_name and stock_quantity.
#3. The username is stored in the variable username.
#4. The buy order is inserted into the database.
#5. The user is redirected to the profile page.
#
#


@login_required
def buy(request):
    if request.method == 'POST':
        form = BuyForm(request.POST)
        if form.is_valid():
            stock_name = form.cleaned_data['stock_name']
            stock_quantity = form.cleaned_data['stock_quantity']
            username = request.user.username
            buy_order = BuyOrder(username=username, stock_name=stock_name, stock_quantity=stock_quantity)
            buy_order.save()
            return redirect('profile')
    else:
        form = BuyForm()
    return render(request, 'buy.html', {'form': form})

