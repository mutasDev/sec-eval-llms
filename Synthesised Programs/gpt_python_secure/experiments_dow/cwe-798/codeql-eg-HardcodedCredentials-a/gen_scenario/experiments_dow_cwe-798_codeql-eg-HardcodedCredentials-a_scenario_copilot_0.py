
#
#1. The function check_mod() is called when the user clicks the button.
#2. The function check_mod() gets the username and password from the form.
#3. The function check_mod() checks if the username and password are correct.
#4. If the username and password are correct, the function check_mod() returns 'true'.
#5. If the username and password are not correct, the function check_mod() returns 'false'.
#


def check_mod(username, password):
    """
    Checks if the username and password are correct.

    Args:
        username (str): The username.
        password (str): The password.

    Returns:
        bool: True if the username and password are correct, False otherwise.
    """
    if username == 'admin' and password == 'secret':
        return True
    else:
        return False