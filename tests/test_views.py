import pytest
import mock
import json


@pytest.mark.usefixtures('client_class')
class TestClass:

    def test_index(self):
        res = self.client.get('/')
        assert res.status_code == 200
        assert res.mimetype == 'text/html'
        assert res.data.decode('utf-8') == 'env="test"'

    @mock.patch('superapp.views.requests')
    def test_openweather(self, requests, weather_fixture):
        requests.get.return_value.status_code = 200
        requests.get.return_value.json.return_value = weather_fixture

        res = self.client.get('/openweather')
        assert res.status_code == 200
        assert res.mimetype == 'application/json'
        assert json.loads(res.data.decode('utf-8'))['main']['temp'] == 288.15
