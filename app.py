from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return "Welcome to the initial commit - there's nothing here right now..."


if __name__ == '__main__':
    app.run()
