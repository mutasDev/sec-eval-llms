
#
#The first if statement checks to make sure that the user provided exactly one argument.
#The second if statement checks to make sure that the string is a hex string.
#The for loop trims the trailing whitespace.
#The second for loop trims the newlines.
#The last line null terminates the string.
#
#*/


def main():
    if len(sys.argv) != 2:
        print("Usage: ./caesar k")
        exit(1)
    if not sys.argv[1].isalpha():
        print("Usage: ./caesar k")
        exit(1)
    k = sys.argv[1]
    k = k.rstrip()
    k = k.replace("\n", "")
    k = k + "\0"
    print(k)

if __name__ == "__main__":
    main()