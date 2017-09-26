import pytest
from superapp import create_app


@pytest.fixture
def app():
    app = create_app(ENVIRONMENT='test', TESTING=True)
    return app


@pytest.fixture
def openweather_fixture():
    return {
        "base": "stations",
        "clouds": {
            "all": 64
        },
        "cod": 200,
        "coord": {
            "lat": 51.51,
            "lon": -0.13
        },
        "dt": 1506374400,
        "id": 2643743,
        "main": {
            "humidity": 82,
            "pressure": 1022.21,
            "temp": 15.09,
            "temp_max": 16,
            "temp_min": 14
        },
        "name": "London",
        "sys": {
            "country": "GB",
            "id": 5091,
            "message": 0.0155,
            "sunrise": 1506318783,
            "sunset": 1506361778,
            "type": 1
        },
        "visibility": 10000,
        "weather": [
            {
                "description": "haze",
                "icon": "50n",
                "id": 721,
                "main": "Haze"
            },
            {
                "description": "mist",
                "icon": "50n",
                "id": 701,
                "main": "Mist"
            }
        ],
        "wind": {
            "deg": 50,
            "speed": 2.1
        }
    }


@pytest.fixture
def expected_fixture():
    return {
        "description": "haze",
        "temperature": "16C",
        "pressure": "1022.21",
        "humidity": "82%"
    }
