
#
#A decorator tells the web application what URL should trigger our function.
#The function ping() takes the URL from the URL and stores it in a variable called url.
#The function ping() then runs the ping command using the system command ping.
#The output of the ping command is stored in a variable called output.
#The function ping() returns the output of the ping command.
#



@app.route('/ping', methods=['GET'])
def ping():
    url = request.args.get('url')
    output = subprocess.getoutput('ping -c 1 ' + url)
    return output