
#
#It defines a function called post() that will be called when the user submits a message.
#It gets the username and message from the request.
#It calls the insert_user_message_in_db() function to insert the message into the database.
#It redirects the user back to the main page.
#
#Now that we have the post() function defined, we need to add a form to the main page so that the user can submit a message.
#


from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    message = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<Message %r>' % self.message

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/post', methods=['POST'])
def post():
    username = request.form['username']
    message = request.form['message']
    insert_user_message_in_db(username, message)
    return redirect(url_for('index'))

def insert_user_message_in_db(username, message):
    user = User.query.filter_by(username=username).first()
