
#
#It defines a function called post() that will be called when the user submits a message.
#It gets the username and message from the request.
#It calls the insert_user_message_in_db() function to insert the message in the database.
#It redirects the user to the main page.
#
#Now, let's add the code to display the messages.
#
#

@app.route('/', methods=['GET'])
def get():
    messages = get_all_messages_from_db()
    return render_template('index.html', messages=messages)
