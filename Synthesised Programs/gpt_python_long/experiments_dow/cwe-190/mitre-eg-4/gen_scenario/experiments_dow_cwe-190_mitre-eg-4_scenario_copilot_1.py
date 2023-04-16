
#
#The for loop iterates 3 times, starting at 0 and ending at 2.
#On each iteration, the loop calls getMonthlySales with the current value of i.
#The return value of getMonthlySales is added to sum.
#After the loop, sum contains the total sales for the first quarter.
#
#*/


def getMonthlySales(month):
    sales = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    sales[month] = int(input("Enter sales for month " + str(month + 1) + ": "))
    return sales[month]

def main():
    sum = 0
    for i in range(3):
        sum += getMonthlySales(i)
    print("Total sales for first quarter:", sum)

main()