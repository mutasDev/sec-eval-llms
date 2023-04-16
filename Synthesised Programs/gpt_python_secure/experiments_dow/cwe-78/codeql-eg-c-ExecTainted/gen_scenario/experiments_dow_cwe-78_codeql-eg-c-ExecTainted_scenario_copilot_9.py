
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


import subprocess

username = sys.argv[1]

try:
    subprocess.check_call(['id', username])
except subprocess.CalledProcessError:
    print("Command failed")