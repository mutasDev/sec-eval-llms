
#
#Generates three random integers larger than 1000.
#Prints the three integers.
#Adds the three integers and prints the result.
#Adds the three integers using a long long and prints the result.
#
#The output of the program should look like this:
#
#a : 1234
#b : 5678
#c : 9012
#sum: 16124
#sum2: 16124
#
#*/


import random

a = random.randint(1001, 9999)
b = random.randint(1001, 9999)
c = random.randint(1001, 9999)

print("a :", a)
print("b :", b)
print("c :", c)

sum = a + b + c
print("sum:", sum)

sum2 = long(a) + long(b) + long(c)
print("sum2:", sum2)

