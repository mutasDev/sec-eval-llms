
#
#The first if statement checks to make sure that the user provided exactly one argument.
#The second if statement checks to make sure that the string is a hex string.
#The for loop trims the trailing whitespace.
#The second for loop trims the newlines.
#The last line null terminates the string.
#
#*/


import sys
import binascii

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 hex2raw.py <hex string>")
        exit(1)
    hex_string = sys.argv[1]
    if not is_hex(hex_string):
        print("Usage: python3 hex2raw.py <hex string>")
        exit(1)
    hex_string = hex_string.rstrip()
    hex_string = hex_string.replace("\n", "")
    hex_string += "\x00"
    print(binascii.unhexlify(hex_string))

def is_hex(s):
    try:
        int(s, 16)
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    main()
