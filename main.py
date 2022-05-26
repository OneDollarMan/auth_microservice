from flask import Flask, render_template, send_from_directory, request
from flask_jwt import JWT, jwt_required, current_identity


class User(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __str__(self):
        return self.username


def safe_str_cmp(string1, string2):
    if len(string1) != len(string2):
        return False
    result = True
    for c1, c2 in zip(string1, string2):
        result &= c1 == c2  # compare all characters one by one
    return result


def unsafe_str_cmp(string1, string2):
    return string1 == string2


users = [
    User(1, 'user1', 'qwerty'),
    User(2, 'user2', 'abcxyz'),
]

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}


def authenticate(username, password):
    user = username_table.get(username, None)
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)


app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'super-secret'

jwt = JWT(app, authenticate, identity)


@app.route('/protected')
@jwt_required()
def protected():
    return 'Hello, %s' % current_identity


@app.route('/auth')
def auth():
    return render_template('auth.html'), 200


@app.route('/script.js')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])


if __name__ == '__main__':
    app.run()
