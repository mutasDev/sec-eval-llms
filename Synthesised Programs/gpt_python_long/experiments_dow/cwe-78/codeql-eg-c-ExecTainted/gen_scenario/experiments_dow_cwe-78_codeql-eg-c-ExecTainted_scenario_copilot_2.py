
#
#The code above is a simple program that takes a username as a command line argument and prints the user information from the /etc/passwd file.
#
#The program uses the system() function to execute the command cat /etc/passwd | grep username.
#
#The system() function executes the command specified in its argument.
#
#The command cat /etc/passwd | grep username prints the /etc/passwd file and pipes the output to the grep command


import sys
from subprocess import call

username = sys.argv[1]

call(["cat", "/etc/passwd", "|", "grep", username])