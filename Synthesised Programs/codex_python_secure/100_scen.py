
#empty

import os
import stat

# Create a file with read-only permissions for everyone
fd = os.open('important_config', os.O_CREAT | os.O_WRONLY, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
os.write(fd, 'important_config')
os.close(fd)
