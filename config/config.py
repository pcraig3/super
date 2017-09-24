try:
    from . import secrets
except:
    raise LookupError(
        'Please create a secrets.py file with an \'OPENWEATHER_KEY\' string'
    )

# Secret Values
OPENWEATHER_KEY = secrets.OPENWEATHER_KEY

# Flask configurations
DEBUG = False
TESTING = False
