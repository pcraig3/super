#!/usr/bin/env python
from superapp import create_app


app = create_app(ENVIRONMENT='prod')


if __name__ == '__main__':
    app.run(port=8080)
