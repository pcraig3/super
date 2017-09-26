import requests

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


views = Blueprint('views', __name__, url_prefix='/weather/london')


@views.errorhandler(APIError)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@views.route('/')
def index():
    return 'env="{}"'.format(current_app.config['ENVIRONMENT'])


@views.route('/openweather')
def openweather():

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

    return jsonify({
        'description':  DescriptionField('weather:0:description').value(_json),
        'temperature':  TemperatureField('main:temp').value(_json, unit=unit),
        'pressure':     PressureField('main:pressure').value(_json),
        'humidity':     HumidityField('main:humidity').value(_json)
    })
