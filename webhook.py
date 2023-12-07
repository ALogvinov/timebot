from flask import Flask, request, jsonify, make_response, abort
import requests

# Создаем объект flask
app = Flask(__name__)


def get_time(latitude: float, longitude: float) -> str:
    """
    Возвращает время и дату по координатам
    :param latitude: широта
    :param longitude: долгота
    :return: дата и время
    """
    url = f"https://timeapi.io/api/Time/current/coordinate?latitude={latitude}&longitude={longitude}"
    response = requests.get(url)
    data = response.json()
    time = data['time']
    date = data['date']
    return f'{date} {time}'


def get_result() -> dict:
    """
    Возвращает ответ боту DW
    :return: словарь с данными для бота
    """
    req = request.get_json(force=True)
    parameters = req['queryResult']['parameters']
    latitude = parameters['latitude']
    longitude = parameters['longitude']
    current_time = get_time(latitude, longitude)
    return {
        'fulfillmentText': current_time
    }


@app.route('/')
def index() -> str:
    """
    Тестовый маршрут для проверки работы сервиса
    :return: 'ok'
    """
    return 'ok'


@app.route('/webhook', methods=['GET', 'POST'])
def webhook() -> str:
    """
    Вебхук для вызова со стороны DW
    :return: json для DW
    """
    return make_response(jsonify(get_result()))


# Запускаем сервер
app.run(host='0.0.0.0', port=81)
