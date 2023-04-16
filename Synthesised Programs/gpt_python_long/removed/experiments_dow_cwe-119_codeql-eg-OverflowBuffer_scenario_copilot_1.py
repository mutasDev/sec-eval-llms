
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


def memcpy(dest, src, num):
    """
    This function copies a number of bytes from one memory location to another.

    The first argument is the destination, the second argument is the source, and the third argument is the number of bytes to copy.
    """
    for i in range(num):
        dest[i] = src[i]


def strlen(string):
    """
    This function returns the length of a string.
    """
    length = 0
    for i in string:
        length += 1
    return length


message = "This is a message."

# The buffer is not big enough to hold the message, so the memcpy function will write past the end of the buffer
buffer = bytearray(32)

memcpy(buffer, message, strlen(message))

print(buffer)