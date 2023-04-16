
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

filename = "secret.txt"

# Write the data to the file
with open(filename, "wb") as f:
    f.write(b"U2FsdGVkX1/R+WzJcxgvX/Iw==")

# Set the permissions of the file
os.chmod(filename, stat.S_IRUSR | stat.S_IWUSR)

# Print the permissions of the file
print("Permissions of {}: {}".format(filename, oct(os.stat(filename).st_mode)[-3:]))