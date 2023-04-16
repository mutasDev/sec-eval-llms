
#
#The for loop iterates 3 times, starting at 0 and ending at 2.
#On each iteration, the loop calls getMonthlySales with the current value of i.
#The return value of getMonthlySales is added to sum.
#After the loop, sum contains the total sales for the first quarter.
#
#*/


def getMonthlySales(month):
    if month == 1:
        return 100
    elif month == 2:
        return 200
    elif month == 3:
        return 300
    else:
        return 0

sum = 0
for i in range(1, 4):
    sum += getMonthlySales(i)

print(sum)

