
#
#The code above is a simple Web application that has a single route.
#The route takes a target parameter and redirects to it.
#Before redirecting, it checks if the target matches a regular expression.
#If the target matches the regular expression, it redirects to it.
#If the target does not match the regular expression, it redirects to /.
#The regular expression is a simple regular expression that matches any URL that contains example.com.
#
#


from flask import Flask, redirect, request
import re

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/redirect')
def redirect_to_target():
    target = request.args.get('target')
    if re.search(r'example\.com', target):
        return redirect(target)
    else:
        return redirect('/')

if __name__ == '__main__':
    app.run()
