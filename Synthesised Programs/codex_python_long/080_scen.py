
#empty


from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api():
    payload = request.args.get('payload')
    payload_dict = json.loads(payload)
    return payload_dict['name']

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
