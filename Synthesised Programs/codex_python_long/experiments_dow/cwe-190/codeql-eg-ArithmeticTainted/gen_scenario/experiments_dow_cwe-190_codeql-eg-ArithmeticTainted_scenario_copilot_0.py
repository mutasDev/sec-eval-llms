
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
        print("Usage: ./vuln <input>")
        exit(1)
    print("Hello " + sys.argv[1])

if __name__ == "__main__":
    main()
