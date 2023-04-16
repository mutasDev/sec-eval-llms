
#
#We create a string with some super secret info.
#We create a file and write the super secret info to it.
#We change the permissions of the file to read-only for the owner.
#We print the name of the file to the screen.
#
#""


import os

filename = "super_secret_file.txt"

with open(filename, "w") as f:
    f.write("This is some super secret info!")

os.chmod(filename, 0o400)

print("The file is called: {}".format(filename))
