
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

def get_quarterly_sales(quarter):
    if quarter == 1:
        return get_monthly_sales() + get_monthly_sales() + get_monthly_sales()
    elif quarter == 2:
        return get_monthly_sales() + get_monthly_sales() + get_monthly_sales()
    elif quarter == 3:
        return get_monthly_sales() + get_monthly_sales() + get_monthly_sales()
    elif quarter == 4:
        return get_monthly_sales() + get_monthly_sales() + get_monthly_sales()

print(get_quarterly_sales(1))
print(get_quarterly_sales(2))
print(get_quarterly_sales(3))
print(get_quarterly_sales(4))