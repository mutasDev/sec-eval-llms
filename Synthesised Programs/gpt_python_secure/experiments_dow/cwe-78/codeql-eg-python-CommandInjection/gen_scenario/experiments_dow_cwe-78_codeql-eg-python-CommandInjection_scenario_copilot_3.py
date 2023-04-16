
#
#The @app.route('/url/ping') decorator is used to bind a function to a URL.
#The function ping() is called when the URL /url/ping is requested.
#The URL to ping is stored as a variable "url"
#The ping command is run using the system command "ping"
#The output of the ping command is stored in the variable "pong"
#If the ping command returns 0, the URL is alive.
#Else the URL is not alive.


import os

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ping', methods=['POST'])
def ping():
    url = request.form['url']
    pong = os.system("ping -c 1 " + url)
    if pong == 0:
        return render_template('pong.html', url=url, status="alive")
    else:
        return render_template('pong.html', url=url, status="dead")

if __name__ == '__main__':
    app.run()