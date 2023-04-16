
#empty


import os
import sys
import stat

def main():
    fd = os.open("important_config", os.O_CREAT | os.O_RDWR, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
    os.write(fd, "important_config")
    os.close(fd)

if __name__ == "__main__":
    main()
