#1. It creates a Flask app.
#2. It defines a route for the app.
#3. It defines a function that will be called when the route is called.
#4. It connects to the database.
#5. It executes a query.
#6. It returns the result of the query.


from flask import Flask, jsonify, abort, make_response, request
import os
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

@app.route('/users', methods=['POST'])
def create_user():
    if not request.json or not 'username' in request.json:
        abort(400)
    user = {
        'id': users[-1]['id'] + 1,
        'username': request.json['username'],
        'password': generate_password_hash(request.json['password']),
        'role' : request.json.get('role', "user")
    }
    users.append(user)
    return jsonify({'user': user}), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = [user for user in users if user['id'] == user_id]
    if len(user) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'username' in request.json and type(request.json['username']) != str:
        abort(400)
    if 'password' in request.json and type(request.json['password']) != str:
        abort(400)
    if 'role' in request.json and type(request.json['role']) != str:
        abort(400)
    user[0]['username'] = request.json.get('username', user[0]['username'])
    user[0]['role'] = request.json.get('role', user[0]['role'])
    user[0]['password'] = generate_password_hash(request.json.get('password', user[0]['password']))
    return jsonify({'user': user[0]})

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = [user for user in users if user['id'] == user_id]
    if len(user) == 0:
        abort(404)
    users.remove(user[0])
    return jsonify({'result': True})

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({'users': users})

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = [user for user in users if user['id'] == user_id]
    if len(user) == 0:
        abort(404)
    return jsonify({'user': user[0]})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    users = [
        {
            'id': 1,
            'username': u'admin',
            'password': generate_password_hash('admin'),
            'role': u'admin'
        },
        {
            'id': 2,
            'username': u'mark',
            'password': generate_password_hash('mark'),
            'role': u'user'
        }
    ]
    app.run(debug=True)