
#empty


import sys
import os
import hashlib

def main():
    if len(sys.argv) != 3:
        print("Usage: {} <input file> <output file>".format(sys.argv[0]))
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    if not os.path.exists(input_filename):
        print("Input file {} does not exist".format(input_filename))
        sys.exit(1)

    if os.path.exists(output_filename):
        print("Output file {} already exists".format(output_filename))
        sys.exit(1)

    with open(input_filename, "rb") as input_file:
        with open(output_filename, "wb") as output_file:
            data = input_file.read()
            checksum = hashlib.md5(data).digest()
            output_file.write(checksum)

if __name__ == "__main__":
    main()