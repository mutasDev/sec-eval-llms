
#
#The redirect_url function takes a url as an argument.
#The urlparse function from the urllib.parse module is used to parse the url.
#The netloc attribute of the parsed_url object is used to get the domain name of the url.
#If the domain name is example.com, the url is redirected to.
#If the domain name is not example.com, a 404 error is returned.
#
#"""




import urllib.parse

def redirect_url(url):
    parsed_url = urllib.parse.urlparse(url)
    domain = parsed_url.netloc
    if domain == "example.com":
        return url
    else:
        return "404"