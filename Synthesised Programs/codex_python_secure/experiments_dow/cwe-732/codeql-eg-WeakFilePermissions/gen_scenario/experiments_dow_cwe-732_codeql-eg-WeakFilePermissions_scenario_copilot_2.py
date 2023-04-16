
#
#We create a file called secret.txt and write the string U2FsdGVkX1/R+WzJcxgvX/Iw== to it.
#
#We then change the permissions of the file to 0000.
#
#This means that the file is not readable, writable or executable by anyone.
#
#If you try to open the file in a text editor, you will get an error.
#
#



import os

# Create a file
f = open("secret.txt", "w")
f.write("U2FsdGVkX1/R+WzJcxgvX/Iw==")
f.close()

# Change the permissions of the file
os.chmod("secret.txt", 0000)

# Try to open the file
f = open("secret.txt", "r")
print(f.read())
f.close()