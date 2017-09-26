import pytest
import mock
import json


@pytest.mark.usefixtures('client_class')
class TestClass:

    def test_index(self):
        res = self.client.get('/')
        assert res.status_code == 200
        assert res.mimetype == 'text/html'
        assert "welcome to my super weather api" in res.data.decode('utf-8')

    @mock.patch('superapp.views.requests')
    def test_weather(
        self, requests, openweather_fixture, expected_fixture
    ):
        requests.get.return_value.status_code = 200
        requests.get.return_value.json.return_value = openweather_fixture

        res = self.client.get('/weather/london/20170926/0309')
        assert res.status_code == 200
        assert res.mimetype == 'application/json'
        assert json.loads(res.data.decode('utf-8')) == expected_fixture

    @mock.patch('superapp.views.requests')
    def test_weather_one_field(
        self, requests, openweather_fixture, expected_fixture
    ):
        requests.get.return_value.status_code = 200
        requests.get.return_value.json.return_value = openweather_fixture

        res = self.client.get('/weather/london/20170926/0309/temperature')
        assert res.status_code == 200
        assert res.mimetype == 'application/json'
        assert json.loads(res.data.decode('utf-8')) == {
            'temperature': expected_fixture['temperature']
        }
