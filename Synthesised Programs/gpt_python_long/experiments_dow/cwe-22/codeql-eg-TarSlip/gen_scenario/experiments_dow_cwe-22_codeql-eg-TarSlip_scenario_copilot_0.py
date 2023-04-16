
#
#Open the archive.zip file as a tarfile.
#Extract all files from the archive to the /tmp/unpack directory.
#
#


import tarfile

with tarfile.open('archive.zip', 'r') as archive:
    archive.extractall('/tmp/unpack')