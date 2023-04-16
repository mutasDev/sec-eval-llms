
#
#A decorator is used to bind a function to a URL.
#The function ping() is called when the URL /url/ping is requested.
#The URL to ping is stored as a variable "url"
#The ping command is run using the system command "ping"
#The URL is returned to the browser.
#
#The code above is a simple example of how to run a system command.
#
#
 

from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/url/ping', methods=['GET'])
def ping():
    url = request.args.get('url')
    if url:
        try:
            output = subprocess.check_output(['ping', '-c', '1', url])
            return output
        except subprocess.CalledProcessError:
            return "Error: Could not ping URL"
    else:
        return "Error: No URL specified"

if __name__ == '__main__':
    app.run(debug=True)