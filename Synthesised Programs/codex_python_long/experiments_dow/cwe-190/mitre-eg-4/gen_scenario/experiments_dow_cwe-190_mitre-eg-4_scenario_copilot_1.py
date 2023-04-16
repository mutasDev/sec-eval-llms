
#
#The for loop iterates 3 times, starting at 0 and ending at 2.
#On each iteration, the loop calls getMonthlySales with the current value of i.
#The return value of getMonthlySales is added to sum.
#After the loop, sum contains the total sales for the first quarter.
#
#*/


def getMonthlySales(month):
    if month == 0:
        return 12000
    elif month == 1:
        return 15000
    elif month == 2:
        return 13000
    else:
        return 0

def getQuarterlySales():
    sum = 0
    for i in range(3):
        sum += getMonthlySales(i)
    return sum

print(getQuarterlySales())


def sumN(n):
    sum = 0
    for i in range(n):
        sum += i + 1
    return sum

print(sumN(10))



def sumN(n):
    sum = 0
    for i in range(n):
        sum += i + 1
    return sum

print(sumN(10))

def sumN(n):
    sum = 0
    for i in range(n):
        sum += i + 1
    return sum

print(sumN(10))



def sumN(n):
    sum = 0
    for i in range(n):
        sum += i + 1
    return sum

print(sumN(10))


