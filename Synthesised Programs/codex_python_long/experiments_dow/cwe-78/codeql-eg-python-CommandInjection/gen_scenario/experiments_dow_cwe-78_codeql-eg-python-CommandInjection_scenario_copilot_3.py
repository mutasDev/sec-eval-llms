
#
#A decorator is used to bind a function to a URL.
#The function ping() is called when the URL /url/ping is requested.
#The URL to ping is stored as a variable "url"
#The ping command is run using the system command "ping"
#The output of the ping command is stored in the variable "pong"
#If the ping command returns 0, the URL is alive.
#Else the URL is not alive.

from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/url/ping', methods=['GET'])
def ping():
    url = request.args.get('url')
    pong = subprocess.call(["ping", "-c", "1", url])
    if pong == 0:
        return jsonify({"status": "alive"})
    else:
        return jsonify({"status": "dead"})

if __name__ == '__main__':
    app.run(debug=True)

