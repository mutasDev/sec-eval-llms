
#empty


import os
import sys
import hashlib

def hash_file(filename):
   """"This function returns the SHA-256 hash
   of the file passed into it"""

   # make sure the file exists
   if not os.path.isfile(filename):
       return None

   # open file for reading in binary mode
   with open(filename, 'rb') as file:
       # hash the file
       hasher = hashlib.sha256()
       while True:
           # read file in as little chunks
           chunk = file.read(1024)
           if not chunk:
               break
           hasher.update(chunk)

       # return the hex representation of the hash
       return hasher.hexdigest()

def main():
   # make sure a filename was provided
   if len(sys.argv) != 2:
       print('Usage: {} filename'.format(sys.argv[0]))
       return

   # calculate the hash of the file
   sha256_hash = hash_file(sys.argv[1])
   print(sha256_hash)

if __name__ == '__main__':
   main()