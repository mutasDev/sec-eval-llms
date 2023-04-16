
#
#It allocates a buffer of size buffer_size.
#It overwrites all values in the buffer with 'A'.
#It does not free the buffer.
#
#The code above is vulnerable to a buffer overflow.
#
#The buffer is allocated on the stack.
#The buffer is not freed.
#The buffer is overwritten with more data than it can hold.
#
#The buffer is allocated on the stack.
#
#The stack is a region of memory that is used

def vulnerable_function(buffer_size):
    buffer = bytearray(buffer_size)
    buffer[:] = b'A' * buffer_size

vulnerable_function(10)