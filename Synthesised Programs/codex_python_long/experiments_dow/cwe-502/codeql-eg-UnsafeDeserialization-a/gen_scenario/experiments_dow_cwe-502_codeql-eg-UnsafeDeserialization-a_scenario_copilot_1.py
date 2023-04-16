
#
#1. We import a web application class from the web application module.
#2. We create an instance of the web application class.
#3. We use the route() decorator to tell the application what URL should trigger our function.
#4. The function is given a name which is also used to generate URLs for that particular function, and returns the message we want to display in the user’s browser.
#5. Finally we have to run the application instance
#


from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()

@app.route('/hello')
def hello_world():
    return 'Hello World'

@app.route('/hello')
def hello_world():
    return 'Hello World'

## Flask URL Building

from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.