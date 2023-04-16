
#
#It defines a function called post() that will be called when the user submits a message.
#It gets the username and message from the request.
#It calls the insert_user_message_in_db() function to insert the message in the database.
#It redirects the user to the main page.
#
#Now, let's add the code to display the messages.
#
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
    messages = Message.query.all()
    return render_template('index.html', messages=messages)

@app.route('/post', methods=['POST'])
def post():
    message = Message(message=request.form['message'], user_id=1)
    db.session.add(message)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()