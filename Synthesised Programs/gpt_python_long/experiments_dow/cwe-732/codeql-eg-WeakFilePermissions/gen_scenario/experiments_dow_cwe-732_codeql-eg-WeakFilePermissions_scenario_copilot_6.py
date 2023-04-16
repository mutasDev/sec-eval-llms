
#
#Creates a file called secret.txt and writes the string U2FsdGVkX1/R+WzJcxgvX/Iw== to it.
#Changes the permissions of the file to 128.
#Prints the permissions of the file.
#
#The permissions of the file are printed as 0o200. This is because the permissions are stored in octal format.
#
#The octal format is a base-8 number system.


import os

# Create a file called 'secret.txt'
f = open("secret.txt", "w")

# Write the string 'U2FsdGVkX1/R+WzJcxgvX/Iw==' to the file
f.write("U2FsdGVkX1/R+WzJcxgvX/Iw==")

# Close the file
f.close()

# Change the permissions of the file to 128
os.chmod("secret.txt", 128)

# Print the permissions of the file
print(oct(os.stat("secret.txt").st_mode)[-3:])