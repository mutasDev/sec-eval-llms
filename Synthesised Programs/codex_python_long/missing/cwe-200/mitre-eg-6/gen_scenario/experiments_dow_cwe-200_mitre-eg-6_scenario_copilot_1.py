
#
#The code above is a simple web application that has a single route /info. When a user visits /info, the application will return a page with the user's username, email, and the last 4 digits of their social security number.
#
#The application has a single vulnerability.


import requests
import json
import sys
import base64
import random
import string

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def main():
    url = "http://localhost:5000/info"
    username = randomString()
    email = randomString() + "@" + randomString() + ".com"
    ssn = randomString()
    payload = {'username': username, 'email': email, 'ssn': ssn}
    r = requests.post(url, data=payload)
    print(r.text)

if __name__ == "__main__":
    main()

