from flask import Flask, request, jsonify, make_response, abort

app = Flask(__name__)


def get_time(latitude, longitude):
    time = '09:16'
    date = "30.11.2023"
    return f'{date} {time}'


def get_result():
    req = request.get_json(force=True)
    current_time = get_time(45.1, 67.2)
    print(current_time)
    return {
        'fulfillmentText': current_time
    }


@app.route('/')
def index():
    return 'Hello from Flask!'


@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    return make_response(jsonify(get_result()))


app.run(host='0.0.0.0', port=81)
