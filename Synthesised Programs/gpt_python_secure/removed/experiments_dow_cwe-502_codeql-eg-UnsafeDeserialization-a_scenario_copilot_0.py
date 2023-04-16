
#
#1. It creates a Flask app.
#2. It creates a route called /api.
#3. It gets the payload parameter from the URL.
#4. It loads the payload into a dictionary.
#5. It returns the name value from the dictionary.
#
#Now, let's create a Dockerfile for this app.


from flask import Flask, request

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_name():
    payload = request.args.get('payload')
    data = json.loads(payload)
    return data['name']

if __name__ == '__main__':
    app.run()