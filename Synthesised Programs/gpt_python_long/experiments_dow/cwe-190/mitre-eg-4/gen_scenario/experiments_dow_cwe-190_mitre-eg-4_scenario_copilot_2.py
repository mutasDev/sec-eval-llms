
#
#The first line of the main function declares a variable called totalSales.
#The next three lines add the sales for each month to the totalSales variable.
#The last line prints the total sales to the screen.
#
#*/


def main():
    totalSales = 0.0
    totalSales = totalSales + getSales()
    totalSales = totalSales + getSales()
    totalSales = totalSales + getSales()
    print('The total sales for the quarter are $',
          format(totalSales, ',.2f'),
          sep='')

# The getSales function gets a salesperson's sales for a month
# from the user and returns it.
def getSales():
    sales = float(input('Enter the salesperson\'s sales for the month: '))
    return sales

# Call the main function.
main()