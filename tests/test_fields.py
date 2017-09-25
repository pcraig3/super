import pytest
from superapp.fields import Field, TemperatureField


class TestFields:

    def test_field(self, weather_fixture):
        f = Field("main:temp")
        assert f.path == 'main:temp'
        assert f._find(weather_fixture) == 288.15
        with pytest.raises(Exception):
            assert f.value(weather_fixture) == 288.15

