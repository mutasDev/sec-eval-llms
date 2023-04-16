
#
#The rand() function generates a random number.
#The RAND_MAX macro defines the maximum value that rand() can return.
#The (float) typecasts the result of the division to a float.
#The print function writes the string representation of a float to a string.
#The %f format specifier is used to write a float to a string.
#The string array is used to store the string representation of the float.
#The string array must be large


import random

def rand_float():
    return random.random()

def main():
    print("%f" % rand_float())

if __name__ == "__main__":
    main()

