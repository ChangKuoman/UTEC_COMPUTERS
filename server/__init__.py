from flask import (
    Flask,
    abort,
    jsonify,
    request,
    render_template
)
from models.MotherBoard import MotherBoard
from models.Component import Component
from models.User import User
from models.Compatible import Compatible
from models.Simulation import Simulation
from models.SimulationComponent import SimulationComponent
from config import setup_db

from server.routes.__init__ import route
import os

def create_app(test_config=None):
    app = Flask(__name__, template_folder=os.getcwd() + r'\server\frontend\templates')
    setup_db(app)
    app.register_blueprint(route)

    @app.route('/', methods=['GET'])
    def index():
        m = MotherBoard.query.all()
        c = Component.query.all()
        cc = Compatible.query.all()
        u = User.query.all()
        s = Simulation.query.all()
        sc = SimulationComponent.query.all()
        print(u, cc, c, m, s, sc)

        return render_template('index.html')
    
    return app