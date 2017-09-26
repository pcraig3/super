import requests

from datetime import datetime, timezone
from flask import current_app, Blueprint, jsonify, request
from .fields import (
    DescriptionField,
    HumidityField,
    PressureField,
    TemperatureField,
    TEMPERATURE_UNITS,
    OPENWEATHER_UNIT_TRANSLATIONS
)
from .errors import APIError


views = Blueprint('views', __name__)


@views.errorhandler(APIError)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@views.route('/')
def index():
    url1 = 'http://localhost:8080/weather/london/' \
        '20170926/0300?unit=kelvin'

    url2 = 'http://localhost:8080/weather/london/' \
        '20170926/0300/pressure?unit=metric'

    return '<p>welcome to my super weather api!</p>'\
        '<p>try these urls: ' \
        '<ul><li><a href="{0}">{0}</a></li>' \
        '<li><a href="{1}">{1}</a></li></ul>'.format(url1, url2)


@views.route('/weather/london/<date_param>/<time_param>')
@views.route('/weather/london/<date_param>/<time_param>/<key>')
def weather(date_param, time_param, key=None):

    # parse the date and the time. throw an error if the format is bad
    try:
        date_param = datetime.strptime(date_param, "%Y%m%d").date()
        time_param = datetime.strptime(time_param, "%H%M").time()
    except ValueError as e:
        raise APIError(e.args[0], status_code=400)

    # combine date and time into start variable, which is a timestamp
    start = datetime.combine(
        date_param, time_param
    ).replace(
        tzinfo=timezone.utc
    ).timestamp()

    unit = request.args.get('unit', 'celcius')
    if unit not in TEMPERATURE_UNITS.keys():
        raise APIError(
            '\'{}\' is not a permitted unit. Valid units are \'{}\''.format(
                unit, '\', \''.join(TEMPERATURE_UNITS.keys())
            ), status_code=400)

    openweather_url = '''
        http://api.openweathermap.org/data/2.5/weather?q=London,uk
        '''

    res = requests.get('{}&appid={}&units={}'.format(
        openweather_url,
        current_app.config['OPENWEATHER_KEY'],
        OPENWEATHER_UNIT_TRANSLATIONS[unit]
    ))

    # if the status code doesn't start with a "2"
    if int('{}'.format(res.status_code)[:1]) != 2:
        raise APIError(res.json()['message'], status_code=res.status_code)

    # okay, so at this point we have a good response
    _json = res.json()

    result = {
        'description':  DescriptionField('weather:0:description').value(_json),
        'temperature':  TemperatureField('main:temp').value(_json, unit=unit),
        'pressure':     PressureField('main:pressure').value(_json),
        'humidity':     HumidityField('main:humidity').value(_json)
    }

    if key:
        if key not in result.keys():
            raise APIError(
                '\'{}\' is not a permitted key. Valid keys are \'{}\''.format(
                    key, '\', \''.join(result.keys())
                ), status_code=400)

        result = {key: result[key]}

    return jsonify(result)
