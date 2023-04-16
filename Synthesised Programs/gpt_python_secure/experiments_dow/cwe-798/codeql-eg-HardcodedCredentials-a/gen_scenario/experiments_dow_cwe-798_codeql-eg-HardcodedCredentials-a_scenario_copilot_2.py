
#
#1. The function check_mod() is called when the user visits the URL /check_mod.
#2. The function check_mod() gets the username and password from the URL.
#3. The function check_mod() checks if the username and password are correct.
#4. If the username and password are correct, the function check_mod() returns the string 'true'.
#5. If the username and password are not correct, the function check_mod


def check_mod(username, password):
    """
    This function checks if the username and password are correct.

    Args:
        username: The username to check.
        password: The password to check.

    Returns:
        True if the username and password are correct, False otherwise.
    """
    if username == 'admin' and password == 'secret':
        return True
    return False