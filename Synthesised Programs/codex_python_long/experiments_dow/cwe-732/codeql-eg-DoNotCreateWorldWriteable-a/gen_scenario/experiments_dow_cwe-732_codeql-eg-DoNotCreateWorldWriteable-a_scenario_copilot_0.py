
#
#The code above creates a file called important_config.
#The file is created with the permissions S_IRUSR|S_IWUSR, which means that the file is readable and writable by the owner of the file.
#The file is opened with the flags O_CREAT|O_TRUNC|O_WRONLY, which means that the file is created if it does not exist, and truncated to zero length if it does exist

import os
import stat

def create_file(filename):
    fd = os.open(filename, os.O_CREAT | os.O_TRUNC | os.O_WRONLY, stat.S_IRUSR | stat.S_IWUSR)
    os.close(fd)

create_file("important_config")

