
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

if len(sys.argv) != 2:
    print("Usage: %s <hex string>" % sys.argv[0])
    sys.exit(1)

hex_string = sys.argv[1]

if not all(c in string.hexdigits for c in hex_string):
    print("Error: input string is not a hex string.")
    sys.exit(1)

hex_string = hex_string.rstrip()
hex_string = hex_string.replace("\n", "")
hex_string += "\x00"

print(binascii.unhexlify(hex_string))
