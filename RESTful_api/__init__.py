from flask import (
    Flask,
    abort,
    jsonify,
    request
)
from flask_cors import CORS
from models.Motherboard import MotherBoard
from models.Component import Component
from models.User import User
from models.Compatible import Compatible
from models.Simulation import Simulation
from models.SimulationComponent import SimulationComponent
from config import setup_db

def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.after_request
    def after_requests(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorizations, true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
        return response

    @app.route('/', methods=['GET'])
    def index():
        m = MotherBoard.query.all()
        c = Component.query.all()
        cc = Compatible.query.all()
        u = User.query.all()
        s = Simulation.query.all()
        sc = SimulationComponent.query.all()
        print(u, cc, c, m, s, sc)

        return jsonify({
            'success': True
        })
    
    return app