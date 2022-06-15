from flask import Blueprint
api = Blueprint('api', __name__)

from server.routes.routes_motherboards import *
from server.routes.routes_simulations import *
from server.routes.routes_simulation_components import *
from server.routes.routes_errors import *
from server.routes.routes_users import *
from server.routes.routes_components import *
from server.routes.routes_compatibles import *