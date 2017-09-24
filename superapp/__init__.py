from flask import Flask


def create_app(**config_overrides):
    app = Flask(__name__)

    # Load default config then apply overrides
    app.config.from_object('config.config')
    app.config.update(config_overrides)

    app.url_map.strict_slashes = False

    from .views import views
    app.register_blueprint(views)

    return app
