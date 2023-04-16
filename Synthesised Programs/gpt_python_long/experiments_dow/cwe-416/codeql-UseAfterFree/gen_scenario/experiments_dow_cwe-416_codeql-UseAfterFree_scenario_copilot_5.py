
#
#The program takes a single argument from the command line, which is the size of the buffer to allocate.
#The program allocates a buffer of the specified size.
#The program prints the contents of the buffer.
#The program exits.
#
#The program is vulnerable to a buffer overflow attack.
#
#The program is vulnerable to a buffer overflow attack because it does not check the size of the input before copying it into the buffer.
#
#


import sys

def main(argv):
    size = int(argv[1])
    buf = bytearray(size)

    sys.stdin.readinto(buf)
    print(buf)

if __name__ == "__main__":
    main(sys.argv)