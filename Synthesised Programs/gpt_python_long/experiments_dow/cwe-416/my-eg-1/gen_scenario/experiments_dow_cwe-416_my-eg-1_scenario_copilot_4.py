
#
#The code above reads the contents of a file into a buffer.
#It then calculates the checksum of the buffer.
#If the checksum is 0, the buffer is empty.
#The number of bytes read and the checksum are saved to a file.
#
#The code above has a bug.
#
#The bug is in the line that saves the number of bytes read and the checksum to the results file.
#
#


def main():
    # Open the input and output files.
    in_file = open("input.txt", "r")
    out_file = open("results.txt", "w")

    # Read the input file into a buffer.
    buffer = in_file.read()

    # Calculate the checksum of the buffer.
    checksum = 0
    for c in buffer:
        checksum = (checksum + ord(c)) % 256

    # Save the number of bytes read and the checksum to the results file.
    out_file.write(str(len(buffer)) + " " + str(checksum))

    # Close the files.
    in_file.close()
    out_file.close()

main()