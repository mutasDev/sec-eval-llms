
#
#The first line of the main function declares a variable called totalSales.
#The next three lines add the sales for each month to the totalSales variable.
#The last line prints the total sales to the screen.
#
#*/


def main():
    totalSales = 0.0
    totalSales = totalSales + getSales(1)
    totalSales = totalSales + getSales(2)
    totalSales = totalSales + getSales(3)
    print('The total sales for the quarter were $', \
          format(totalSales, ',.2f'), sep='')

def getSales(month):
    # Get the amount of sales for a month.
    # Return the amount entered.
    sales = float(input('Enter the sales for month ' + \
                        str(month) + ': '))
    return sales

# Call the main function.
main()