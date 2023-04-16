
#
#1. The function check_mod() is called when the user clicks the button.
#2. The function check_mod() gets the username and password from the form.
#3. The function check_mod() checks if the username and password are correct.
#4. If the username and password are correct, the function check_mod() returns 'true'.
#5. If the username and password are not correct, the function check_mod() returns 'false'.
#



def check_mod(username, password):
    if username == 'admin' and password == 'admin':
        return True
    else:
        return False
