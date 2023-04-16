
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


def main():
    buffer = bytearray(100)
    message = "hello world"
    length = len(message)

    if length > len(buffer):
        print("Message is too long")

    # secure implementation
    secure_memcpy(buffer, message, length)


def secure_memcpy(dest, src, length):
    if length > len(dest):
        print("Message is too long")
        return

    for i in range(length):
        dest[i] = src[i]

main()