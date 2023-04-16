
#
#The first line imports the web application class. An instance of this class will be our WSGI application.
#
#The second line creates the application object.
#
#The third line is a decorator. It tells the application which URL should call the associated function.
#
#The fourth line is the function that is called when the user visits the specified URL.
#
#The fifth line returns the message to the user.
#
#The sixth line runs the application.
#


from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()

