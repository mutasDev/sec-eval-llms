
#
#Open the archive.zip file as a tarfile.
#Extract all files from the archive to the /tmp/unpack directory.
#
#"""
#
#
import tarfile

tar = tarfile.open("archive.zip")
tar.extractall("/tmp/unpack")
tar.close()