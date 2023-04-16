
#
# A decorator is used to bind a function to a URL.
#
#The function hello() is called when a user visits the URL /hello/<username> .
#
#The function hello() returns a rendered template, which includes the contents of the template file hello.html, as well as the value of the username variable.
#
#The username variable is passed to the template hello.html, which displays the value of the variable.
#
#


from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hello/<username>')
def hello(username):
    return render_template('hello.html', name=username)

if __name__ == '__main__':
    app.run(debug=True)