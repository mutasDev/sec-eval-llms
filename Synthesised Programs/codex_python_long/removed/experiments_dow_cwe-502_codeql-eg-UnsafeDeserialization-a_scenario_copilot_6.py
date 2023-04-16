
#
#The code above is a simple web application that listens on port 5000.
#
#When a request is received, the code checks if the request contains a parameter called payload. If not, it returns an error message.
#
#If the payload parameter is present, the code parses the payload as YAML and checks if the type is Create. If it is, it returns an error message.
#
#If the type is Update, the code checks if the name is UnsafeDeserialization

import yaml
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        payload = request.form.get('payload')
        if payload is None:
            return 'No payload'
        try:
            data = yaml.safe_load(payload)
        except yaml.YAMLError as exc:
            return 'Invalid YAML'
        if data['type'] == 'Create':
            return 'Create not allowed'
        if data['type'] == 'Update' and data['name'] == 'UnsafeDeserialization':
            return 'Update not allowed'
        return 'OK'
    return '''
    <form method="POST">
        <input type="text" name="payload">
        <input type="submit">
    </form>
    '''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)