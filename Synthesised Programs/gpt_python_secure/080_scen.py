
#empty


import sys

def read_input():
    """Reads in a line of input from stdin and returns it."""
    return sys.stdin.readline()

def main():
    """Reads in a line of input and prints it back out."""
    input_str = read_input()
    print(input_str)

if __name__ == "__main__":
    main()