
#
#The code above takes an integer as input and returns the value at the index of the integer in the array.
#
#For example, if the input is 5, the code will return the value at index 5 of the array.
#
#If the input is out of bounds, the code will return -1.
#
#For example, if the input is 10, the code will return -1.
#
#The code above is vulnerable to a buffer overflow attack.
#
#Your


import random
import string

VULNERABLE = True

def generate_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("Random string of length", length, "is:", result_str)
    return result_str

def main():
    if VULNERABLE:
        buffer_size = 10
        buffer = generate_string(buffer_size)
        print("Buffer is at", hex(id(buffer)))
        print("Buffer size is", buffer_size)
        print("Buffer is", buffer)
        print("Calling vulnerable function...")
        vulnerable_function(buffer)
    else:
        print("Calling protected function...")
        protected_function()

def vulnerable_function(buffer):
    print("Inside vulnerable function")
    print("Buffer is at", hex(id(buffer)))
    print("Buffer size is", len(buffer))
    print("Buffer is", buffer)
    print("Vulnerable function is calling gets()...")
    gets(buffer)
    print("Returned from gets()")
    print("Buffer is", buffer)
    print("Vulnerable function is returning")

def protected_function():
    print("Inside protected function")
    print("Protected function is returning")

main()
