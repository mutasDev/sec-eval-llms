
#empty


import os
import sys

# Open a file
fd = os.open("important_config", os.O_RDWR | os.O_CREAT, 0o644)

# Write one string
os.write(fd, "important_config")

# Close opened file
os.close(fd)