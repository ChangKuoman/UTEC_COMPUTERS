from flask import Flask
from flask_cors import CORS
from config import setup_db

from RESTful_api.routes.__init__ import api

def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app)
    app.register_blueprint(api)

    @app.after_request
    def after_requests(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorizations, true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
        return response

    return app