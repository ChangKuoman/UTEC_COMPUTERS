from flask import Blueprint
api = Blueprint('api', __name__)

from RESTful_api.routes.routes_motherboards import *
from RESTful_api.routes.routes_simulations import *
from RESTful_api.routes.routes_simulation_components import *
from RESTful_api.routes.routes_errors import *
