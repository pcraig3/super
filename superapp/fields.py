import math


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
        """
        Returns a value from a parsed json object
        self.path is expected to be a colon-separated string describing the
        path through the json to the value that we want
        """
        _value = json
        for p in self.path.split(':'):
            try:
                _value = _value[p]
            except TypeError:
                # integer values refer to list items
                _value = _value[int(p)]

        return _value

    def _transform(self, value, **kwargs):
        """
        This method must be overwritten in subclasses
        """
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
        return '{}{}'.format(
            math.ceil(value), TEMPERATURE_UNITS[kwargs['unit']]
        )
