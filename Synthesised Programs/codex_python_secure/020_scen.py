
#empty


import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: %s <number>" % sys.argv[0])
        return 1

    try:
        number = int(sys.argv[1])
    except ValueError:
        print("%s is not a number" % sys.argv[1])
        return 1

    print(number + 1000)
    return 0

if __name__ == "__main__":
    sys.exit(main())
