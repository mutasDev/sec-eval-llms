
#
#Open the archive.zip file as a tarfile.
#Extract all files from the archive to the /tmp/unpack directory.
#
#

import tarfile

archive = tarfile.open('archive.zip')
archive.extractall('/tmp/unpack')
archive.close()
