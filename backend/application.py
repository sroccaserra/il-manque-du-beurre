from flask import Flask

from il_manque_du_beurre.presentation.api import api


def create_app():
    app = Flask(__name__)
    app.register_blueprint(api)
    return app


application = create_app()
