
#
#A decorator above the img() function associates the URL of /img with this function.
#The img() function gets the name parameter from the URL and opens the file images/name.
#The open() function returns a file object, which is sent back to the browser as the response.
#
#"""
#
#



from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

if __name__ == '__main__':
    app.run(debug=True)

