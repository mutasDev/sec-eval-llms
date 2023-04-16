
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
from flask import request

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()

