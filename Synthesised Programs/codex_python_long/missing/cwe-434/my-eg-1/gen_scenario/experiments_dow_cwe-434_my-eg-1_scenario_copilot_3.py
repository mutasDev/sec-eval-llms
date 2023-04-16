
#
#1. I have a form in my html page that allows me to upload a pdf file.
#2. I have a web server that is running on my localhost.
#3. I want to upload the pdf file to my web server and save it in a folder called uploads.
#

import requests

url = "http://localhost:8080/upload"

payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"file\"; filename=\"C:\\Users\\user\\Desktop\\test.pdf\"\r\nContent-Type: application/pdf\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'cache-control': "no-cache",
    'postman-token': "c8f9b8f7-f8f5-f8f8-f8f8-f8f8f8f8f8f8"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
