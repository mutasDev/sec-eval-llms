
#
#1. It checks if the email exists in the database. If it doesn't, it returns 0.
#2. If it does, it calls a php script that unsubscribes the email.
#3. If the php script returns 0, it returns 1. If not, it returns 0.
#
#

import requests
import json

def unsubscribe(email):
    url = "http://localhost:8080/unsubscribe"
    payload = {'email': email}
    headers = {'content-type': 'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    if response.status_code == 200:
        return 1
    else:
        return 0

