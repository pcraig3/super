from flask import current_app, Blueprint, jsonify
import requests

views = Blueprint('views', __name__, url_prefix='/weather/london')


@views.route('/')
def index():
    return 'env="{}"'.format(current_app.config['ENVIRONMENT'])


@views.route('/openweather')
def openweather():
    openweather_url = '''
        http://api.openweathermap.org/data/2.5/weather?q=London,uk
        '''
    res = requests.get('{}&appid={}&units=metric'.format(
        openweather_url, current_app.config['OPENWEATHER_KEY']))

    # if the status code doesn't start with a "2"
    if int('{}'.format(res.status_code)[:1]) != 2:
        raise ValueError(
            '''
            GET request for "{}" returned a status code of "{}".
            Message: "{}"
            '''.format(
                openweather_url, res.status_code, res.json()['message']))

    # okay, so at this point we have a good response
    return jsonify(res.json())
