import pytest


@pytest.mark.usefixtures('client_class')
class TestClass:

    def test_app(self):
        res = self.client.get('/')
        assert res.status_code == 200
        assert res.mimetype == 'text/html'
        assert res.data.decode('utf-8') == 'env="test"'
