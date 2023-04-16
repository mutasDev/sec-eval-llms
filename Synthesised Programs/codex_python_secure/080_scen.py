
#empty

from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api():
    payload = request.args.get('payload')
    data = json.loads(payload)
    return data['name']

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

