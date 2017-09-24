import pytest
from flask import url_for


@pytest.mark.usefixtures('client_class')
class TestClass:

    def test_app(self):
        assert self.client.get(url_for('views.two')).status_code == 404
