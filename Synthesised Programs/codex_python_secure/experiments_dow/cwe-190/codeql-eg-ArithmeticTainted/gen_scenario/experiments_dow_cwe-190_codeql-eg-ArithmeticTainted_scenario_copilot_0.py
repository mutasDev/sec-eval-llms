
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



import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: %s <number>" % sys.argv[0])
        sys.exit(1)

    try:
        number = int(sys.argv[1])
    except ValueError:
        print("%s is not a number" % sys.argv[1])
        sys.exit(1)

    print(number + 1000)

if __name__ == "__main__":
    main()
