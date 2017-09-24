import pytest
from superapp import create_app


@pytest.fixture
def app():
    app = create_app(ENVIRONMENT='test', TESTING=True)
    return app
