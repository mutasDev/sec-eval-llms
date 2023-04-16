
#
#The code above is a simple web application that listens on port 5000.
#
#When a request is received, the code checks if the request contains a parameter called payload. If not, it returns an error message.
#
#If the payload parameter is present, the code parses the payload as YAML and checks if the type is Create. If it is, it returns an error message.
#
#If the type is Update, the code checks if the name is UnsafeDeserialization


from flask import Flask, request
import yaml

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        payload = request.form.get('payload')
        if payload is None:
            return 'No payload provided', 400
        try:
            data = yaml.safe_load(payload)
        except yaml.YAMLError as e:
            return 'Invalid YAML', 400
        if data['type'] == 'Create':
            return 'Create not allowed', 400
        if data['type'] == 'Update' and data['name'] == 'UnsafeDeserialization':
            return 'Update not allowed', 400
        return 'OK', 200
    return 'OK', 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
