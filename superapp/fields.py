TEMPERATURE_UNITS = {
    'metric': 'C',
    'celcius': 'C',
    'kelvin': 'K',
    'fahrenheit': 'F',
    'imperial': 'F'
}


class Field(object):

    def __init__(self, path):
        self.path = path

    def _find(self, json):
        _value = json
        for p in self.path.split(':'):
            try:
                _value = _value[p]
            except TypeError:
                _value = _value[int(p)]

        return _value

    def _transform(self, value, **kwargs):
        raise NotImplementedError('Ack, please implement')

    def value(self, json, **kwargs):
        return self._transform(self._find(json), **kwargs)


class DescriptionField(Field):

    def _transform(self, value, **kwargs):
        return value


class HumidityField(Field):

    def _transform(self, value, **kwargs):
        return '{}%'.format(value)


class PressureField(Field):

    def _transform(self, value, **kwargs):
        return '{}'.format(value)


class TemperatureField(Field):

    def _transform(self, value, **kwargs):
        return '{}{}'.format(int(value), TEMPERATURE_UNITS[kwargs['unit']])
