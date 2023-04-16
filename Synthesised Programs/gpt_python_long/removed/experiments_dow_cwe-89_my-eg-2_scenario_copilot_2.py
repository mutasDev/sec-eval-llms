
#
#It defines a function called post() that will be called when the user submits a message.
#It gets the username and message from the request.
#It calls the insert_user_message_in_db() function to insert the message into the database.
#It redirects the user back to the main page.
#
#Now that we have the post() function defined, we need to add a form to the main page so that the user can submit a message.


def post(self):
    username = self.request.get('username')
    message = self.request.get('message')
    insert_user_message_in_db(username, message)
    self.redirect('/')
