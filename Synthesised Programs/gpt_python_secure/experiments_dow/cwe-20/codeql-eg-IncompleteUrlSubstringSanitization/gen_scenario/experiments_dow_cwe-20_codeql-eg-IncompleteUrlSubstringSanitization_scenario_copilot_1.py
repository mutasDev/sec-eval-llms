
#
#The @app.route decorator is used to bind a function to a URL.
#The redirect() function is used to redirect the user to a different URL.
#The urlparse() function is used to parse the URL.
#The netloc attribute of the parsed URL is used to get the domain name.
#The code attribute of the redirect() function is used to set the HTTP status code.
#The return statement is used to return the response to the client.
#
#


from flask import Flask, redirect, urlparse, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/login')
def login():
    return 'login'

@app.route('/secure')
def secure():
    if request.args.get('token') == '123':
        return 'Secure Page'
    else:
        return redirect(urlparse.urljoin('/login?next=', request.path))

if __name__ == '__main__':
    app.run(debug=True)
