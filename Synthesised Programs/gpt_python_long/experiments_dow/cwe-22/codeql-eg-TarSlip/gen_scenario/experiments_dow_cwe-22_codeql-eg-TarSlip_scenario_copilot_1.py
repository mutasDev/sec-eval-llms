
#
#Open the archive.zip file as a tarfile.
#Extract all files from the archive to the /tmp/unpack directory.
#
#"""
#
#


import tarfile

myTar = tarfile.open('archive.zip')
myTar.extractall('/tmp/unpack')
myTar.close()