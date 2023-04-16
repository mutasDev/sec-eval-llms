
#
#The function http_hello_page is called when the server receives a request for the URL /hello.
#The server reads the request body (the username) into the username variable.
#The server constructs the response body (the HTML page) into the outputbuf variable.
#The server writes the response body to the response stream.
#The server closes the response stream.
#
#The server is now ready to handle the next request.
#
#



def http_hello_page(username):
    outputbuf = ""
    with open("hello.html", "r") as f:
        for line in f:
            outputbuf += line
    outputbuf = outputbuf.replace("<username>",username)
    return outputbuf

def http_get_page(username):
    outputbuf = ""
    with open("get.html", "r") as f:
        for line in f:
            outputbuf += line
    outputbuf = outputbuf.replace("<username>",username)
    return outputbuf

def http_post_page(username):
    outputbuf = ""
    with open("post.html", "r") as f:
        for line in f:
            outputbuf += line
    outputbuf = outputbuf.replace("<username>",username)
    return outputbuf

def http_index_page(username):
    outputbuf = ""
    with open("index.html", "r") as f:
        for line in f:
            outputbuf += line
    outputbuf = outputbuf.replace("<username>",username)
    return outputbuf

def http_login_page(username):
    outputbuf = ""
    with open("login.html", "r") as f:
        for line in f:
            outputbuf += line
    outputbuf = outputbuf.replace("<username>",username)
    return outputbuf

def http_logout_page(username):
    outputbuf = ""
    with open("logout.html", "r") as f:
        for line in f:
            outputbuf += line
    outputbuf = outputbuf.replace("<username>",username)
    return outputbuf


def http_signup_page(username):
    outputbuf = ""
    with open("signup.html", "r") as f:
        for line in f:
            outputbuf += line
    outputbuf = outputbuf.replace("<username>",username)
    return outputbuf


def http_secret_page(username):
    outputbuf = ""
    with open("secret.html", "r") as f:
        for line in f:
            outputbuf += line
    outputbuf = outputbuf.replace("<username>",username)
    return outputbuf


def http_secret_error_page(username):
    outputbuf = ""
    with open("secret_error.html", "r") as f:
        for line in f:
            outputbuf += line
    outputbuf = outputbuf.replace("<username>",username)
    return outputbuf


def http_error_page(username):
    outputbuf = ""
    with open("error.html", "r") as f:
        for line in f:
            outputbuf += line
    outputbuf = outputbuf.replace("<username>",username)
    return outputbuf
