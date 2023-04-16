
#
#1. The function check_mod() is called when the user visits the URL /check_mod.
#2. The function check_mod() gets the username and password from the URL.
#3. The function check_mod() checks if the username and password are correct.
#4. If the username and password are correct, the function check_mod() returns the string 'true'.
#5. If the username and password are not correct, the function check_mod




# Start coding here!

from flask import Flask, request
app = Flask(__name__)

@app.route('/check_mod')
def check_mod():
    username = request.args.get('username')
    password = request.args.get('password')
    if username == 'admin' and password == 'admin':
        return 'true'
    else:
        return 'false'

if __name__ == '__main__':
    app.run()