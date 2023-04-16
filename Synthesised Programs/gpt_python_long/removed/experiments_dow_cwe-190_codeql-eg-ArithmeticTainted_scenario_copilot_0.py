
#
#The code above reads in a value from the command line and adds 1000 to it.
#
#The code above is vulnerable to a buffer overflow attack.
#
#The code above is vulnerable to a format string attack.
#
#The code above is vulnerable to a stack smashing attack.
#
#The code above is vulnerable to a heap overflow attack.
#
#The code above is vulnerable to a return-to-libc attack.


def main():
    num = int(input("Enter a number: "))
    num += 1000
    print("The new number is:", num)

main()