
#
#The code above is a simple login page that takes the username and password from the user and checks if the username and password are correct. If they are correct, the user is redirected to the session page. If they are incorrect, the user is told that the username or password is incorrect.
#


def login_page():
    username = input("Username: ")
    password = input("Password: ")
    if username == "admin" and password == "password":
        print("You have been logged in.")
    else:
        print("Incorrect username or password.")

login_page()