import pytest
from superapp import create_app


@pytest.fixture
def app():
    app = create_app('test')
    return app
