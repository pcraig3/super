from flask import current_app, Blueprint, jsonify
import requests

views = Blueprint('views', __name__)

tasks = [
    {
        "description": "Milk, Cheese, Pizza, Fruit, Tylenol",
        "done": False,
        "id": 1,
        "title": "Buy groceries"
    },
    {
        "description": "Need to find a good Python tutorial on the web",
        "done": False,
        "id": 2,
        "title": "Learn Python"
    }
]


@views.route('/')
def index():
    return 'env="{}"'.format(current_app.config['ENVIRONMENT'])


@views.route('/openweather')
def openweather():
    openweather_url = '''
        http://api.openweathermap.org/data/2.5/weather?q=London,uk
        '''
    res = requests.get('{}&appid={}'.format(
        openweather_url, current_app.config['OPENWEATHER_KEY']))

    # if the status code doesn't start with a "2"
    if int('{}'.format(res.status_code)[:1]) != 2:
        raise ValueError(
            '''
            GET request for "{}" returned a status code of "{}".
            Message: "{}"
            '''.format(
                openweather_url, res.status_code, res.json()['message']))

    return jsonify(res.json())


@views.route('/json')
def json():
    return jsonify({'tasks': tasks})
