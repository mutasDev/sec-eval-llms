
#
#The memcpy function copies a number of bytes from one memory location to another.
#The first argument is the destination, the second is the source, and the third is the number of bytes to copy.
#The strlen function returns the length of a string.
#The code above copies the string "Hello" to the buffer.
#
#The memcpy function is a very useful function, but it has a problem.
#
#The problem is that it doesn't check for the length of the memory.


import ctypes

def memcpy(dest, src, n):
    for i in range(n):
        ctypes.memset(dest + i, ctypes.memget(src + i, 1), 1)

def strlen(s):
    i = 0
    while ctypes.memget(s + i, 1):
        i += 1
    return i

def main():
    buf = ctypes.create_string_buffer(32)
    memcpy(buf, "Hello", strlen("Hello"))

if __name__ == "__main__":
    main()
