
#
#We create a file called secret.txt and write the string U2FsdGVkX1/R+WzJcxgvX/Iw== to it.
#
#We then change the permissions of the file to 0000.
#
#This means that the file is not readable, writable or executable by anyone.
#
#If you try to open the file in a text editor, you will get an error.
#
#


import base64

def encrypt(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode('utf-8')).decode('utf-8')

def decrypt(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode('utf-8')
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

key = 'mysecretkey'
clear = 'secret message'
enc = encrypt(key, clear)
print(enc)
dec = decrypt(key, enc)
print(dec)