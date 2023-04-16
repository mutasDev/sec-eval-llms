
#
#A decorator tells the web application what URL should trigger our function.
#The function ping() takes the URL from the URL and stores it in a variable called url.
#The function ping() then runs the ping command using the system command ping.
#The output of the ping command is stored in a variable called output.
#The function ping() returns the output of the ping command.
#
#"""
 

import subprocess
from flask import Flask
app = Flask(__name__)

@app.route('/ping/<url>')
def ping(url):
    output = subprocess.check_output(['ping', '-c', '3', url])
    return output

if __name__ == '__main__':
    app.run(debug=True)
