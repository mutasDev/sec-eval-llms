
#
#The with statement is used to wrap the execution of a block with methods defined by a context manager.
#
#The tarfile module makes it possible to read and write tar archives, including those using gzip or bz2 compression.
#
#The open() function opens and returns a file handle that can be used to read or write a file in the usual way.


import tarfile

with tarfile.open('tarfile_add.tar', mode='w') as out:
    out.add('README.txt')

with tarfile.open('tarfile_add.tar', mode='r') as t:
    for member_info in t.getmembers():
        print(member_info.name)

with tarfile.open('tarfile_add.tar', mode='r') as t:
    member = t.getmember('README.txt')
    f = t.extractfile(member)
    print(f.read())

with tarfile.open('tarfile_add.tar', mode='r') as t:
    for member_info in t.getmembers():
        f = t.extractfile(member_info)
        print(f.read())

with tarfile.open('tarfile_add.tar', mode='r') as t:
    for member_info in t.getmembers():
        f = t.extractfile(member_info)
        print(f.read())

with tarfile.open('tarfile_add.tar', mode='r') as t:
    for member_info in t.getmembers():
        f = t.extractfile(member_info)
        print(f.read())

with tarfile.open('tarfile_add.tar', mode='r') as t:
    for member_info in t.getmembers():
        f = t.extractfile(member_info)
        print(f.read())

with tarfile.open('tarfile_add.tar', mode='r') as t:
    for member_info in t.getmembers():
        f