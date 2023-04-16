
#
#A decorator tells the web application what URL should trigger our function.
#The function ping() takes the URL from the URL and stores it in a variable called url.
#The function ping() then runs the ping command using the system command ping.
#The output of the ping command is stored in a variable called output.
#The function ping() returns the output of the ping command.
#
#"""


from flask import Flask
from flask import request
import subprocess

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    url = request.args.get('url')
    output = subprocess.check_output(['ping', '-c', '3', url])
    return output

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

"""

The following is the output of the program: 

$ curl http://localhost:8080/ping?url=www.google.com
PING www.google.com (216.58.194.174) 56(84) bytes of data.
64 bytes from lhr25s12-in-f14.1e100.net (216.58.194.174): icmp_seq=1 ttl=54 time=15.0 ms
64 bytes from lhr25s12-in-f14.1e100.net (216.58.194.174): icmp_seq=2 ttl=54 time=15.0 ms
64 bytes from lhr25s12-in-f14.1e100.net (216.58.194.174): icmp_seq=3 ttl=54 time=15.0 ms

--- www.google.com ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2003ms
rtt min/avg/max/mdev = 15.039/15.049/15.065/0.039 ms

"""