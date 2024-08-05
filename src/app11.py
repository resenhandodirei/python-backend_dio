from flask import Flask, url_for, request, jsonify

app = Flask(__name__)

@app.route('/hello-world/<string:user>/<int:age>/<float:height>')
def hello_world(user, age, height):


    return {
        "User": user, 
        "Age": age, 
        "Height": height,
    }

@app.route("/welcome")
def welcome():
    return "<h1>Welcome</h1>"

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about', methods=["GET", "POST"])
def about():
    if request.method == "GET":
        return 'The about page'
    else:
        return "This is a POST"

@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('welcome'))
    print(url_for('projects', next='/'))
    print(url_for('profile', username='John Doe'))
    print(url_for('hello_world', user='John Doe', age=29, height=1.63))

if __name__ == '__main__':
    app.run(debug=True)
