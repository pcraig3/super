# super weather api

- Python app, based on the [Flask framework](http://flask.pocoo.org/)

## Setup

Install [Virtualenv](https://virtualenv.pypa.io/en/latest/)

```
sudo easy_install virtualenv
```

You also need to have a `python3` available globally.

Bootstrap you development environment

```
./scripts/bootstrap.sh
```

### Activate the virtual environment

```source ./venv/bin/activate```

### Run the tests

```py.test```

```flake8 superapp tests```

### Run the api

```./app.py```

##### and then

--> [http://localhost:8080/](http://localhost:8080/) <--

🎉🎉🎉
