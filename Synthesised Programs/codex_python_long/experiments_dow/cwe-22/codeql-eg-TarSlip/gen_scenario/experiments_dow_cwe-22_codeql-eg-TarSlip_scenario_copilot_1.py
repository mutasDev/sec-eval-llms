
#
#Open the archive.zip file as a tarfile.
#Extract all files from the archive to the /tmp/unpack directory.
#
#"""
#
#


import tarfile
import os

def main():
    # Open the tarfile for reading
    tfile = tarfile.open("archive.zip", "r:gz")
    # Create the destination directory
    os.mkdir("/tmp/unpack")
    # Extract all members of the archive to the destination directory
    tfile.extractall("/tmp/unpack")
    # Close the file
    tfile.close()

if __name__ == "__main__":
    main()

"""

The tarfile module provides the following methods for extracting files from an archive:

extractall(path=None, members=None, *, numeric_owner=False)
Extract all members from the archive to the current working directory or specified path.

extract(member, path=None, *, numeric_owner=False)
Extract a member from the archive to the current working directory or specified path.

extractfile(member)
Extract a member from the archive as a file object.

"""