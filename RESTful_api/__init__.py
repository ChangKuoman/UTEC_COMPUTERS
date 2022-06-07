from flask import (
    Flask,
    abort,
    jsonify,
    request
)
from flask_cors import CORS
from models.MotherBoard import MotherBoard
from models.Component import Component
from models.User import User
from models.Compatible import Compatible
from models.Simulation import Simulation
from models.SimulationComponent import SimulationComponent
from config import setup_db

from RESTful_api.routes.__init__ import route

def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app)
    app.register_blueprint(route)

    @app.after_request
    def after_requests(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorizations, true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
        return response

    @app.route('/motherboards/<id>', methods=['DELETE'])
    def delete_motherboards(id):
        error_404 = False
        try:
            motherboard_to_delete = MotherBoard.query.filter(MotherBoard.id==id).one_or_none()

            if motherboard_to_delete is None:
                error_404 = True
                abort(404)
            
            motherboard_to_delete.delete()

            motherboards = MotherBoard.query.order_by('id').all()
            formatted_motherboards = {motherboard.id: motherboard.format() for motherboard in motherboards}
            return jsonify({
                'success': True,
                'deleted': id,
                'motherboard': formatted_motherboards,
                'total_motherboard': len(motherboards)
            })

        except Exception as e:
            print(e)
            if error_404:
                abort(404)
            else:
                abort(500)
              

    @app.route('/components', methods=['GET'])
    def get_components():
        selection_component = Component.query.order_by('id').all()
 
        if len(selection_component) == 0:
            abort(404)
        
        lists_component = {list.id: list.format() for list in selection_component}
        
        return jsonify({
            'success': True,
            'components': lists_component,
            'total_components': len(selection_component)
        })
    
    @app.route('/components/<id>', methods=['DELETE'])
    def delete_componet(id):
        error_404 = False
        try:
            components = Component.query.filter(Component.id==id).one_or_none()

            if components is None:
                error_404 = True
                abort(404)
            
            components.delete()

            selection = components.query.order_by('id').all()
            lists_component = {list.id: list.format() for list in selection}

            return jsonify({
                'success': True,
                'deleted_ID': id,
                'com': lists_component,
                'total_componets': len(selection)
            })

        except Exception as e:
            print(e)
            if error_404:
                abort(404)
            else:
                abort(500)

            


    @app.errorhandler(404)
    def error_404(error):
        return jsonify({
            'success': False,
            'code': 404,
            'message': 'Resource Not Found'
        }), 404

    @app.errorhandler(500)
    def error_500(error):
        return jsonify({
            'success': False,
            'code': 500,
            'message': 'Internal Server Error'
        }), 500
    
    @app.errorhandler(422)
    def error_422(error):
        return jsonify({
            'success': False,
            'code': 422,
            'message': 'Unprocessable'
        }), 422

    return app