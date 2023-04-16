
#
#The code above executes the command getent passwd <username> and stores the output in the file pointer output.
#
#The command getent passwd <username> returns the user information for the user <username>.
#
#The command getent passwd <username> is executed by the system() function.
#
#The command getent passwd <username> is executed by the popen() function.
#
#


import subprocess

username = input("Enter username: ")

try:
    output = subprocess.check_output(["getent", "passwd", username])
except subprocess.CalledProcessError:
    print("User does not exist")
else:
    print(output)
