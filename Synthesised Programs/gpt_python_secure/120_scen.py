
#empty


import os
import sys
import ctypes

def main():
    first_chunk = ctypes.create_string_buffer(10)
    second_chunk = ctypes.create_string_buffer(10)

    # Copy the contents of the first chunk into the second chunk.
    ctypes.memmove(second_chunk, first_chunk, 10)

    # Print the contents of the second chunk.
    sys.stdout.write(second_chunk.raw)

if __name__ == "__main__":
    main()