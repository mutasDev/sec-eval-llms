
#empty


import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: %s <value>" % sys.argv[0])
        return 1
    value = int(sys.argv[1])
    value += 1000
    print(value)
    return 0

if __name__ == "__main__":
    sys.exit(main())
