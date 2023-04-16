
#
#It creates a new route called /post.
#It gets the username and message from the request.
#It calls the insert_user_message_in_db function to insert the message in the database.
#It redirects the user to the / route.
#
#Now, let's add the code to display the messages.
#
#


@app.route('/')
def index():
    messages = get_all_messages_from_db()
    return render_template('index.html', messages=messages)

@app.route('/post', methods=['POST'])
def post():
    username = request.form['username']
    message = request.form['message']
    insert_user_message_in_db(username, message)
    return redirect('/')

if __name__ == '__main__':
    app.run()