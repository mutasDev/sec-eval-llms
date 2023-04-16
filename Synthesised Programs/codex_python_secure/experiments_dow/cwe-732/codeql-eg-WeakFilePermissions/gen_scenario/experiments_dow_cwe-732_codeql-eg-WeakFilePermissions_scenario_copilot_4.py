
#
#We create a string with some super secret info.
#We create a file and write the super secret info to it.
#We change the permissions of the file to read-only for the owner.
#We print the name of the file to the screen.
#
#""



#!/usr/bin/env python

import os

# Create a string with some super secret info.
secret_info = "This is a secret"

# Create a file and write the super secret info to it.
f = open("secret.txt", "w")
f.write(secret_info)
f.close()

# Change the permissions of the file to read-only for the owner.
os.chmod("secret.txt", 0400)

# Print the name of the file to the screen.
print("The secret file is called secret.txt")