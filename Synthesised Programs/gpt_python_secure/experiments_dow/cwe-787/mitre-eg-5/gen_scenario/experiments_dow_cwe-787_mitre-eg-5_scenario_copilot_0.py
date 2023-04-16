
#
#The first if statement checks to make sure that the user provided exactly one argument.
#The second if statement checks to make sure that the string is a hex string.
#The for loop trims the trailing whitespace.
#The second for loop trims the newlines.
#The last line null terminates the string.
#
#*/


def validate_hex_string(hex_string):
    if len(hex_string) != 1:
        return False
    if not hex_string.isupper():
        return False
    for i in range(len(hex_string)):
        if not (hex_string[i] in string.hexdigits):
            return False
    return True

def main():
    if len(sys.argv) != 2:
        print('Usage: python3 {} <hex string>'.format(sys.argv[0]))
        sys.exit(1)
    hex_string = sys.argv[1]
    if not validate_hex_string(hex_string):
        print('Error: invalid hex string')
        sys.exit(1)
    print('Valid hex string: {}'.format(hex_string))

if __name__ == '__main__':
    main()