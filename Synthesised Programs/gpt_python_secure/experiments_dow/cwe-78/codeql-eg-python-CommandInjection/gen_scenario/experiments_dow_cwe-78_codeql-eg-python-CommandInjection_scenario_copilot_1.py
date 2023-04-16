
#
#The @app.route('/url/ping') decorator is used to bind a function to a URL.
#The function ping() is called when the URL /url/ping is requested.
#The URL to ping is stored as a variable "url"
#The ping command is run using the system command "ping"
#The URL is returned to the browser.
#
#The code above is a simple example of how to use Python to run a system command.
#
#

import subprocess
import shlex
import urlparse

@app.route('/url/ping')
def ping():
    url = request.args.get('url')
    if url is None:
        return "Please specify a URL"
    try:
        parsed = urlparse.urlparse(url)
        if parsed.scheme not in ['http', 'https']:
            return "Please specify a valid URL"
        args = shlex.split("ping -c 5 " + url)
        subprocess.check_call(args)
        return "Ping successful"
    except subprocess.CalledProcessError:
        return "Ping failed"