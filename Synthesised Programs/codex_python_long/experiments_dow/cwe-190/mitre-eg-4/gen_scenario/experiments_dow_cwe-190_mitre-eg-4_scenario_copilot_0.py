
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


def getMonthlySales(month):
    return random.randint(0, 100000)

def getQuarterlySales(quarter):
    return getMonthlySales(quarter * 3 - 2) + getMonthlySales(quarter * 3 - 1) + getMonthlySales(quarter * 3)

def getYearlySales():
    return getQuarterlySales(1) + getQuarterlySales(2) + getQuarterlySales(3) + getQuarterlySales(4)

print(getYearlySales())

