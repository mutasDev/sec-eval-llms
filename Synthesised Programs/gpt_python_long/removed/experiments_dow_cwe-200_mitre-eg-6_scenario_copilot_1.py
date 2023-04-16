
#
#The code above is a simple web application that has a single route /info. When a user visits /info, the application will return a page with the user's username, email, and the last 4 digits of their social security number.
#
#The application has a single vulnerability.


import flask

app = flask.Flask(__name__)

@app.route('/info')
def info():
    user = flask.request.args.get('user')
    email = flask.request.args.get('email')
    ssn = flask.request.args.get('ssn')

    return """
    <html>
    <body>

    <h1>User Information</h1>

    <p>Username: {}</p>
    <p>Email: {}</p>
    <p>SSN: {}</p>

    </body>
    </html>
    """.format(user, email, ssn)

if __name__ == '__main__':
    app.run()