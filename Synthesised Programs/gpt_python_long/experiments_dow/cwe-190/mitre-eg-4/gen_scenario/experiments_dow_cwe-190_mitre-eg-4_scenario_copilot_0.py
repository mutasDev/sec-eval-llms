
#
#The code above calls the getMonthlySales function 12 times, once for each month of the year.
#
#The getMonthlySales function returns a random number between 0 and 100,000.
#
#The code above adds up the sales for each quarter and prints the results.
#
#The code above is not very efficient.
#
#If you wanted to add up the sales for the first quarter, you would have to call the getMonthlySales function three times.
#


def get_monthly_sales():
    return random.randint(0, 100000)

def get_quarterly_sales():
    return get_monthly_sales() + get_monthly_sales() + get_monthly_sales()

def get_yearly_sales():
    return get_quarterly_sales() + get_quarterly_sales() + get_quarterly_sales() + get_quarterly_sales()

print(get_yearly_sales())