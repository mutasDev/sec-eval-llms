
#
#The code above is a simple Flask application that has a route /redirect/<url> that takes a URL as a parameter.
#
#The function redirect_invalid_url() checks if the URL is from example.com. If it is, it redirects the user to the URL. If it is not, it returns an error message.
#
#


from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/redirect/<url>')
def redirect_invalid_url(url):
    if not url.startswith('http://example.com'):
        return redirect(url_for('error'))
    return redirect(url)

@app.route('/error')
def error():
    return 'Invalid URL'

if __name__ == '__main__':
    app.run()
