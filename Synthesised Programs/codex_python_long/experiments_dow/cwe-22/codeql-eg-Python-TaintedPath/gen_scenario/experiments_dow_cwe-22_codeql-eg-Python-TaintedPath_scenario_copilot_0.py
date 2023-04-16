
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

@app.route('/img/<name>')
def img(name):
    return open('images/' + name).read()

if __name__ == '__main__':
    app.run(debug=True)


"""

The following code is a simple example of a CGI script that prints one line to standard output: 

#!/usr/bin/python

print "Content-type: text/html"
print
print "<title>Test CGI</title>"
print "<p>Hello World!</p>"

"""