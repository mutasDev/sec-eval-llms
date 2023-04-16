
#
#The memcpy function copies a number of bytes from one memory location to another.
#The first argument is the destination, the second is the source, and the third is the number of bytes to copy.
#The strlen function returns the length of a string.
#The code above copies the string "Hello" to the buffer.
#
#The memcpy function is a very useful function, but it has a problem.
#
#The problem is that it doesn't check for the length of the memory.

def copy_string(dest, src):
    if len(src) > len(dest):
        raise Exception("Source string is too long")
    for i in range(len(src)):
        dest[i] = src[i]
