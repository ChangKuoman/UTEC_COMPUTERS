from flask import Blueprint
route = Blueprint('route', __name__)

from server.routes.routes_errors import *
from server.routes.routes_session import *
