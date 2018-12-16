from flask import Flask

from app.middlewares import error_handler, after_request
from app.models import db
from app.views import *


def create_app(*config_cls) -> Flask:
    flask_app: Flask = Flask(__name__)

    for config in config_cls:
        flask_app.config.from_object(config)

    db.init_app(flask_app)
    db.create_all(app=flask_app)

    flask_app.register_error_handler(Exception, error_handler)
    flask_app.after_request(after_request)

    flask_app.add_url_rule(rule='/register', methods=['POST'],
                           endpoint='register_shorten_url', view_func=register_shorten_url)
    flask_app.add_url_rule(rule='/<shorten_url>', methods=['GET'],
                           endpoint='redirect_original_url', view_func=redirect_original_url)

    return flask_app
