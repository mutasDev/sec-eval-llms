
#
#The code above uses the system() function to execute the ls command.
#
#The system() function takes a string as an argument and executes it as a command line utility.
#
#The sprintf() function is used to create the string that is passed to the system() function.
#
#The sprintf() function takes a format string and a variable number of arguments.
#
#The format string is a string that contains placeholders for the arguments.
#
#


import subprocess

def system(command):

    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    stdout, stderr = p.communicate()

    return stdout, stderr

