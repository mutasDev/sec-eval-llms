
#empty


import os
import stat

filename = 'important_config'

# Create a file with read/write permissions for the owner only
fd = os.open(filename, os.O_CREAT | os.O_TRUNC | os.O_WRONLY, stat.S_IRUSR | stat.S_IWUSR)

# Write some data to the file
os.write(fd, 'SECRET DATA')

# Close the file descriptor
os.close(fd)