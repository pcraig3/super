from flask import Flask

def create_app(config_name):
    app = Flask(__name__)
    app.config['ENVIRONMENT'] = config_name
    app.url_map.strict_slashes = False

    from .views import views
    app.register_blueprint(views)

    return app
