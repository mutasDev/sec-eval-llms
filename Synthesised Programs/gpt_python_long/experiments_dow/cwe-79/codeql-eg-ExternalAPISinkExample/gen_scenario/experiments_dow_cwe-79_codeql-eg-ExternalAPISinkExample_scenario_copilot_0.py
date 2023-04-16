
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
    outputbuf = "<html><body>Hello, " + username + "!</body></html>"
    return outputbuf