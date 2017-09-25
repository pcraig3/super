import pytest
from superapp.fields import (
    Field, DescriptionField, HumidityField, PressureField,  TemperatureField
    )


def test_field(openweather_fixture):
    f = Field("main:temp")
    assert f.path == 'main:temp'
    assert f._find(openweather_fixture) == 15.09
    with pytest.raises(Exception):
        assert f.value(openweather_fixture) == 15.09


def test_description_field(openweather_fixture):
    f = DescriptionField("weather:0:description")
    assert f.value(openweather_fixture) == "haze"


def test_humidity_field(openweather_fixture):
    f = HumidityField("main:humidity")
    assert f.value(openweather_fixture) == "82%"


def test_pressure_field(openweather_fixture):
    f = PressureField("main:pressure")
    assert f.value(openweather_fixture) == "1022.21"


def test_temperature_field(openweather_fixture):
    f = TemperatureField("main:temp")
    assert f.value(openweather_fixture, unit="metric") == "15C"
