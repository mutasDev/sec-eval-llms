
#
#Creates a file called secret.txt and writes the string U2FsdGVkX1/R+WzJcxgvX/Iw== to it.
#Changes the permissions of the file to 128.
#Prints the permissions of the file.
#
#The permissions of the file are printed as 0o200. This is because the permissions are stored in octal format.
#
#The octal format is a base-8 number system.

import os
import stat

# Create a file
f = open("secret.txt", "w")
f.write("U2FsdGVkX1/R+WzJcxgvX/Iw==")
f.close()

# Change the permissions of the file
os.chmod("secret.txt", stat.S_IREAD)

# Print the permissions of the file
print(oct(os.stat("secret.txt").st_mode))
