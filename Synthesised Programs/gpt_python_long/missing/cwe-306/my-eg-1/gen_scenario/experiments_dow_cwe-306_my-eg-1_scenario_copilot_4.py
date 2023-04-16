
#
#The login page is a simple form with a username and password field.
#
#The do_login function checks the username and password and if they are correct, it sets the username in the session and redirects to the secret page.
#
#The index page is a simple page that has a link to the login page.
#
#The secret page is a simple page that says “Secret settings”.
#



from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = 'ThisIsSecret' # you need to set a secret key for security purposes

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/login', methods=['POST'])
def do_login():

  if request.form['password'] == 'password' and request.form['username'] == 'admin':
    session['logged_in'] = True
  else:
    flash('wrong password!')
  return home()

@app.route("/logout")
def logout():
  session['logged_in'] = False
  return home()

@app.route("/home")
def home():
  if not session.get('logged_in'):
    return render_template('login.html')
  else:
    return "Hello Boss!  <a href='/logout'>Logout</a>"

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)



