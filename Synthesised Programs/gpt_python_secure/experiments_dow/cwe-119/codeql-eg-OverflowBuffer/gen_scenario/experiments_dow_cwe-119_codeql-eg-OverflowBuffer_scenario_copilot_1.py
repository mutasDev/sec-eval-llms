
#
#The memcpy function copies a number of bytes from one memory location to another.
#
#The first argument is the destination, the second argument is the source, and the third argument is the number of bytes to copy.
#
#The strlen function returns the length of a string.
#
#The code above copies the message to the buffer.
#
#The buffer is not big enough to hold the message, so the memcpy function will write past the end of the buffer


def copy_message(dest, src, length):
    if len(dest) < length:
        raise ValueError('Destination too small')
    for i in range(length):
        dest[i] = src[i]