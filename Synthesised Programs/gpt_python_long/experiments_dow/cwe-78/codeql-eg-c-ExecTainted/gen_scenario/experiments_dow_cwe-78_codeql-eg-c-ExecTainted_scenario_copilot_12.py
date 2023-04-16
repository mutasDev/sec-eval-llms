
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

username = input("Enter the username: ")

# Option 1
output = subprocess.getoutput("getent passwd " + username)

# Option 2
# output = subprocess.check_output("getent passwd " + username, shell=True)

# Option 3
# output = subprocess.call("getent passwd " + username, shell=True)

print(output)