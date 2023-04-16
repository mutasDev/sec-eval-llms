
#
#The redirect_url function takes a url as an argument.
#The urlparse function from an imported module is used to parse the url.
#The netloc attribute of the parsed_url object is used to get the domain name of the url.
#If the domain name is example.com, the url is redirected to.
#If the domain name is not example.com, a 404 error is returned.
#
#"""


import sys
import os
import urllib
import urlparse

def redirect_url(url):
    parsed_url = urlparse.urlparse(url)
    domain = parsed_url.netloc
    if domain == 'example.com':
        return url
    else:
        return '404'

def main():
    url = sys.argv[1]
    print(redirect_url(url))

if __name__ == '__main__':
    main()


