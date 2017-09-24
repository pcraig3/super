import pytest
from flask import url_for


@pytest.mark.usefixtures('client_class')
class TestClass:

    def test_app(self):
        res = self.client.get(url_for('views.json'))
        assert res.status_code == 200
        assert res.mimetype == 'application/json'
        assert res.json['tasks'][0]['id'] == 1
