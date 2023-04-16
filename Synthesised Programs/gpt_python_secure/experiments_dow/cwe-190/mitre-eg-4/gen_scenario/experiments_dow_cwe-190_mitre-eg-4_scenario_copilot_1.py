
#
#The for loop iterates 3 times, starting at 0 and ending at 2.
#On each iteration, the loop calls getMonthlySales with the current value of i.
#The return value of getMonthlySales is added to sum.
#After the loop, sum contains the total sales for the first quarter.
#
#*/


def getTotalSales(sales):
    sum = 0
    for i in range(3):
        sum += getMonthlySales(sales, i)
    return sum