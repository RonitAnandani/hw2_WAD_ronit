from flask import Flask
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app= Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "user": generate_password_hash("user"),
    "guest": generate_password_hash("guest")
}

@auth.verify_password
def verify_password(username, password):
    if username in users:
        return check_password_hash(users.get(username), password)
    return False

@app.route('/')
@auth.login_required
def index():
    return "Hello, %s!" % auth.username()

if   __name__ == '__main__':
    print(users)
    app.run(host='locathost', port=5002, debug=True)    