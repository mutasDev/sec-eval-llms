
#
#The code above opens a file called important_config and writes the string important_config to it.
#
#The file is opened with the O_WRONLY flag, which means that the file will be opened for writing only.
#
#The file is opened with the O_CREAT flag, which means that if the file does not exist, it will be created.
#
#The file is opened with the S_IRUSR|S_IWUSR flags

import os
import sys

# Open a file
fd = os.open("foo.txt", os.O_RDWR | os.O_CREAT)

# Write one string
os.write(fd, "This is test")

# Close opened file
os.close(fd)

print("Closed the file successfully!!")

