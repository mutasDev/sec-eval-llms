
#
#The function http_hello_page takes in a request and a response.
#The request is a file stream that contains the request from the client.
#The response is a file stream that we can write to.
#The request contains the username that the client entered.
#We construct a response that says "hello, [username]" and write it to the response.
#The response is sent back to the client.
#
#The function escape_html is a function that escapes HTML


import cgi

def escape_html(s):
    return cgi.escape(s, quote = True)

def http_hello_page(request, response):
    username = request.readline().strip()
    response.write("hello, " + escape_html(username))