
#
#The code above is a simple program that takes a username as a command line argument and prints the user information from the /etc/passwd file.
#
#The program uses the system() function to execute the command cat /etc/passwd | grep username.
#
#The system() function executes the command specified in its argument.
#
#The command cat /etc/passwd | grep username prints the /etc/passwd file and pipes the output to the grep command


import os
import sys

username = sys.argv[1]

os.system("cat /etc/passwd | grep " + username)


import os
import sys
import re

username = sys.argv[1]

if re.search(r";", username) or re.search(r"&", username):
    print("Input is not valid")
else:
    os.system("cat /etc/passwd | grep " + username)
