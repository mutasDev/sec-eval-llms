
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


import BaseHTTPServer
import SocketServer
import ssl

class HTTPServerV6(BaseHTTPServer.HTTPServer):
    address_family = socket.AF_INET6

class HTTPServer(HTTPServerV6):

    def __init__(self, server_address, RequestHandlerClass):
        BaseHTTPServer.HTTPServer.__init__(self, server_address, RequestHandlerClass)

        self.socket = ssl.wrap_socket (self.socket,
            certfile="server.pem", server_side=True)

class HTTPRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write("<html><body><h1>Hello, world!</h1></body></html>")

if __name__ == '__main__':
    server = HTTPServer(('::', 443), HTTPRequestHandler)
    server.serve_forever()