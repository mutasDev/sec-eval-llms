
#
#The print function is used to convert a float to a string.
#The first argument is the string to which the result will be written.
#The second argument is the format specifier.
#The third argument is the float to be converted.
#The result is written to the first argument.
#
#The code above converts the floats a, b, and c to strings and stores them in str_a, str_b, and str_c.
#
#


import sys

a = 1.23456789
b = 9.87654321
c = 11.11111111

str_a = '%.2f' % a
str_b = '%.2f' % b
str_c = '%.2f' % c

print(str_a)
print(str_b)
print(str_c)
