
#
#The code above is a simple login page that takes the username and password from the user and checks if the username and password are correct. If they are correct, the user is redirected to the session page. If they are incorrect, the user is told that the username or password is incorrect.
#


from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    session['name'] = request.form['name']
    session['email'] = request.form['email']
    return redirect('/show')

@app.route('/show')
def show_user():
    return render_template('user.html')

app.run(debug=True)