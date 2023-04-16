
#
#The rand() function generates a random number.
#The RAND_MAX macro defines the maximum value that rand() can return.
#The (float) typecasts the result of the division to a float.
#The print function writes the string representation of a float to a string.
#The %f format specifier is used to write a float to a string.
#The string array is used to store the string representation of the float.
#The string array must be large


import random

MAX_NUMBER = 100

def main():
    for i in range(10):
        number = random.randint(1, MAX_NUMBER)
        print(number)

if __name__ == "__main__":
    main()