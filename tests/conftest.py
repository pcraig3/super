import pytest
from superapp import create_app


@pytest.fixture
def app():
    app = create_app(ENVIRONMENT='test', TESTING=True)
    return app


@pytest.fixture
def weather_fixture():
    return {
            'main': {
                'humidity': 93,
                'pressure': 1019,
                'temp': 288.15,
                'temp_max': 289.15,
                'temp_min': 287.15
            }
        }
