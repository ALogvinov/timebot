from flask import Flask, request, jsonify, make_response, abort

app = Flask(__name__)


def get_result():
    req = request.get_json(force=True)
    print(req)


@app.route('/')
def index():
    return 'Hello from Flask!'


@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    return make_response(jsonify(get_result()))


app.run(host='0.0.0.0', port=81)
