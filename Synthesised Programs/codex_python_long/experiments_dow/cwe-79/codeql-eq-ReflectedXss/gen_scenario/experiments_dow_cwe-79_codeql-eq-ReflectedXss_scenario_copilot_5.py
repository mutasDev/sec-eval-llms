
#
#A decorator creates a mapping between the URL given as an argument and the function that follows it.
#
#The function hello() returns a string with the text Hello, followed by the value of the variable username.
#
#The variable username is passed as an argument to the function hello().
#
#The escape() function converts special characters to HTML-safe sequences.
#
#The function hello() is called when a user navigates to the URL /hello/username


from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/hello/<username>')
def hello(username):
    return 'Hello, {}!'.format(escape(username))

if __name__ == "__main__":
    app.run(debug=True)

