import logging
from sys import stdout, stderr
from flask import Flask, request

app = Flask(__name__)

log = logging.getLogger()

stdout_handler = logging.StreamHandler(stdout)
stdout_handler.setLevel(logging.DEBUG)
stdout_handler.addFilter(lambda record: record.levelno <= logging.INFO)

stderr_handler = logging.StreamHandler(stderr)
stderr_handler.setLevel(logging.WARNING)

log.addHandler(stdout_handler)
log.addHandler(stderr_handler)


@app.route('/')
def hello_world():  # put application's code here
    return "Welcome to the initial commit - there's nothing here right now..."


@app.route('/oauth')
def oauth_endpoint():
    returned_state = request.args.get('state')
    returned_code = request.args.get('code')
    returned_error = request.args.get('error')

    if returned_error:
        return f"Oauth failed due to error: {returned_error}"

    return f"Oauth Endpoint\nState: {returned_state}\nCode: {returned_code}"


if __name__ == '__main__':
    app.run()
