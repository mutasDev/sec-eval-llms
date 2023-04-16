
#
#The @app.route('/url/ping') decorator tells Flask what URL should trigger our function.
#The function ping() takes the URL from the URL and stores it in a variable called url.
#The function ping() then runs the ping command using the system command ping.
#The output of the ping command is stored in a variable called output.
#The function ping() returns the output of the ping command.
#
#"""


import subprocess

def ping(url):
    cmd = ['ping', '-c', '3', url]
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = proc.communicate()
    return stdout
