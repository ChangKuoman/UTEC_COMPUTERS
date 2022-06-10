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

    #COMPONENT

    @app.route('/component', methods=['GET'])
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
    
    @app.route('/component', methods=['POST'])
    def create_component():
        body = request.get_json()

        description = body.get('description', None)
        completed = body.get('completed', None)
        list_id = body.get('list_id', None)
        search = body.get('search', None)

        if search:
            selection = Component.query.order_by('id').filter(Component.description.like(f'%{search}%')).all()
            list_components = {list.id: list.format() for list in selection}
            return jsonify({
                'success': True,
                'components': todos,
                'total_components': len(selection)
            })

        if description is None or list_id is None:
            abort(422)

        componet = Component(description=description, completed=completed, list_id=list_id)
        new_component_id = componet.insert()

        selection = Component.query.order_by('id').all()
        list_components = {list.id: list.format() for list in selection}

        return jsonify({
            'success': True,
            'created': new_component_id,
            'components': list_components,
            'total_components': len(selection)
        })
    
    @app.route('/component/<id>', methods=['PATCH'])
    def update_component(id):
        error_404 = False
        try:
            component = Component.query.filter(Component.id==id).one_or_none()

            if component is None:
                error_404 = True
                abort(404)
            
            body = request.get_json()
            if 'description' in body:
                component.description = body.get('description')
            
            component.update()

            return jsonify({
                'success': True,
                'id': component.id
            })
        except Exception as e:
            print(e)
            if error_404:
                abort(404)
            else:
                abort(500)

    @app.route('/component/<id>', methods=['DELETE'])
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

                'components': lists_component,
                'total_componets': len(selection)
            })

        except Exception as e:
            print(e)
            if error_404:
                abort(404)
            else:
                abort(500)
 
    #COMPATIBLE

    @app.route('/compatible', methods=['GET'])
    def get_components():
        selection_compatible = Compatible.query.order_by('id').all()
 
        if len(selection_compatible) == 0:
            abort(404)
        
        lists_compatible = {list.id: list.format() for list in selection_compatible}
        
        return jsonify({
            'success': True,
            'components': lists_compatible,
            'total_components': len(selection_compatible)
        })
    
    @app.route('/compatible', methods=['POST'])
    def create_Compatible():
        body = request.get_json()

        description = body.get('description', None)
        completed = body.get('completed', None)
        list_id = body.get('list_id', None)
        search = body.get('search', None)

        if search:
            selection = Compatible.query.order_by('id').filter(Compatible.description.like(f'%{search}%')).all()
            list_Compatible = {list.id: list.format() for list in selection}
            return jsonify({
                'success': True,
                'Compatibles': list_Compatible,
                'total_Compatibles': len(selection)
            })

        if description is None or list_id is None:
            abort(422)

        compatible = Compatible(description=description, completed=completed, list_id=list_id)
        new_compatible_id = compatible.insert()

        selection = Compatible.query.order_by('id').all()
        list_Compatible = {list.id: list.format() for list in selection}

        return jsonify({
            'success': True,
            'created': new_compatible_id,
            'Compatibles': list_Compatible,
            'total_Compatibles': len(selection)
        })
    
    @app.route('/compatible/<id>', methods=['PATCH'])
    def update_compatible(id):
        error_404 = False
        try:
            compatible = Compatible.query.filter(Compatible.id==id).one_or_none()

            if compatible is None:
                error_404 = True
                abort(404)
            
            body = request.get_json()
            if 'description' in body:
                Compatible.description = body.get('description')
            
            compatible.update()

            return jsonify({
                'success': True,
                'id': compatible.id
            })
        except Exception as e:
            print(e)
            if error_404:
                abort(404)
            else:
                abort(500)
    

    @app.route('/compatible/<id>', methods=['DELETE'])
    def delete_componet(id):
        error_404 = False
        try:
            compatible = Compatible.query.filter(Compatible.id==id).one_or_none()

            if compatible is None:
                error_404 = True
                abort(404)
            
            compatible.delete()

            selection = Compatible.query.order_by('id').all()
            lists_compatible = {list.id: list.format() for list in selection}

            return jsonify({
                'success': True,
                'deleted_ID': id,
                'compatibles': lists_compatible,
                'total_componets': len(selection)
            })

        except Exception as e:
            print(e)
            if error_404:
                abort(404)
            else:
                abort(500)

    #USERS

    @app.route('/users', methods=['GET'])
    def get_():
        selection_users = User.query.order_by('id').all()
 
        if len(selection_users) == 0:
            abort(404)
        
        lists_users = {list.id: list.format() for list in selection_users}
        
        return jsonify({
            'success': True,
            'users': lists_users,
            'total_users': len(selection_users)
        })
    
    @app.route('/users', methods=['POST'])
    def create_Users():
        body = request.get_json()

        description = body.get('description', None)
        completed = body.get('completed', None)
        list_id = body.get('list_id', None)
        search = body.get('search', None)

        if search:
            selection = User.query.order_by('id').filter(User.description.like(f'%{search}%')).all()
            list_users = {list.id: list.format() for list in selection}
            return jsonify({
                'success': True,
                'Users': list_users,
                'total_Users': len(selection)
            })

        if description is None or list_id is None:
            abort(422)

        user = User(description=description, completed=completed, list_id=list_id)
        new_user_id = user.insert()

        selection = User.query.order_by('id').all()
        list_Users = {list.id: list.format() for list in selection}

        return jsonify({
            'success': True,
            'created': new_user_id,
            'Users': list_Users,
            'total_Users': len(selection)
        })
    
    @app.route('/users/<id>', methods=['PATCH'])
    def update_User(id):
        error_404 = False
        try:
            user = User.query.filter(User.id==id).one_or_none()

            if user is None:
                error_404 = True
                abort(404)
            
            body = request.get_json()
            if 'description' in body:
                User.description = body.get('description')
            
            user.update()

            return jsonify({
                'success': True,
                'id': user.id
            })
        except Exception as e:
            print(e)
            if error_404:
                abort(404)
            else:
                abort(500)
    

    @app.route('/users/<id>', methods=['DELETE'])
    def delete_user(id):
        error_404 = False
        try:
            user = User.query.filter(User.id==id).one_or_none()

            if user is None:
                error_404 = True
                abort(404)
            
            user.delete()

            selection = User.query.order_by('id').all()
            lists_Users = {list.id: list.format() for list in selection}

            return jsonify({
                'success': True,
                'deleted_ID': id,
                'Users': lists_Users,
                'total_users': len(selection)
            })

        except Exception as e:
            print(e)
            if error_404:
                abort(404)
            else:
                abort(500)

    return app