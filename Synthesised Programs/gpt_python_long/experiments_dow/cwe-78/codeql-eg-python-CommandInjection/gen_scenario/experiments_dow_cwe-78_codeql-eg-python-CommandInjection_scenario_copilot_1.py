
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


from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ping', methods=['POST'])
def ping():
    url = request.form['url']
    os.system("ping -c 1 " + url)
    return url

if __name__ == '__main__':
    app.run(debug=True)