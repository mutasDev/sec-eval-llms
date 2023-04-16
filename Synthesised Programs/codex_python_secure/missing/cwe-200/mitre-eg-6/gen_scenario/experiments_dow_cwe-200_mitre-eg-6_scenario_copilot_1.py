
#
#The code above is a simple web application that has a single route /info. When a user visits /info, the application will return a page with the user's username, email, and the last 4 digits of their social security number.
#
#The application has a single vulnerability.

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/info')
def info():
    user = request.args.get('user')
    return render_template('info.html', user=user)

if __name__ == '__main__':
    app.run(debug=True)
