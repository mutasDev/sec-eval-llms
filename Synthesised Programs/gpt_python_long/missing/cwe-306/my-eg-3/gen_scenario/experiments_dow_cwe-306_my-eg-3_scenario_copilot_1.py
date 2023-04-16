
#
#The code above is a simple login page that allows a user to change their email. The user must be logged in to change their email. The user must provide their old email, new email, and confirm password. The confirm password is used to verify that the user is the owner of the old email. The user must provide an existing email. The user must provide the correct confirm password. If the user provides the correct information, the email is changed.
#
#


@app.route('/change-email', methods=['GET', 'POST'])
def change_email():
    if not session.get('logged_in'):
        abort(401)
    form = ChangeEmailForm(request.form)
    if form.validate_on_submit():
        old_email = form.old_email.data
        new_email = form.new_email.data
        password = form.password.data
        if session['email'] == old_email and check_password_hash(session['password'], password):
            session['email'] = new_email
            flash('Email changed')
        else:
            flash('Invalid email or password')
    return render_template('change_email.html', form=form)