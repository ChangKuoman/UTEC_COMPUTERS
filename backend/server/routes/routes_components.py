from flask import abort, jsonify, request
from models.Component import Component
from server.routes.__init__ import api
from models.User import User


@api.route('/components', methods=['GET'])
def get_components():
    selection_components = Component.query.order_by('id').all()

    if len(selection_components) == 0:
        abort(404)

    dictionary_components = {component.id: component.format() for component in selection_components}
    return jsonify({
        'success': True,
        'components': dictionary_components,
        'total_components': len(selection_components)
    })


@api.route('/components/<id>', methods=['GET'])
def get_component(id):
    component = Component.query.filter(Component.id==id).one_or_none()

    if component is None:
        abort(404)

    dictionary_component = component.format()
    selection_component = Component.query.order_by('id').all()
    return jsonify({
        'success': True,
        'component': dictionary_component,
        'total_components': len(selection_component)
    })


@api.route('/components/<id>', methods=['DELETE'])
def delete_component(id):
    error_404 = False
    try:
        component_to_delete = Component.query.filter(Component.id==id).one_or_none()

        if component_to_delete is None:
            error_404 = True
            abort(404)

        component_to_delete.delete()

        selection_components = component_to_delete.query.order_by('id').all()
        dictionary_components = {component.id: component.format() for component in selection_components}
        return jsonify({
            'success': True,
            'deleted_id': id,
            'components': dictionary_components,
            'total_components': len(selection_components)
        })
    except Exception as e:
        print(e)
        if error_404:
            abort(404)
        else:
            abort(500)


@api.route('/components/<id>', methods=['PATCH'])
def patch_component(id):
    error_404 = False
    error_422 = False
    error_401 = False
    error_403 = False
    try:
        component_to_patch = Component.query.filter(Component.id==id).one_or_none()

        if component_to_patch is None:
            error_404 = True
            abort(404)

        body = request.get_json()
        if 'token' not in body:
            error_422 = True
            abort(422)
        user = User.check_token(body.get('token'))
        if user is None:
            error_401 = True
            abort(401)
        if user.role != 'admin':
            error_403 = True
            abort(403)

        component_to_patch.modify_by = user.id
        if 'description' in body:
            component_to_patch.description = body.get('description')
        if 'price' in body:
            component_to_patch.price = body.get('price')
        if 'type' in body:
            component_to_patch.component_type = body.get('type')
        if 'name' in body:
            component_to_patch.name = body.get('name')

        updated_id = component_to_patch.update()
        if updated_id is None:
            error_422 = True
            abort(422)

        selection_components = Component.query.order_by('id').all()
        dictionary_components = {component.id: component.format() for component in selection_components}
        return jsonify({
            'success': True,
            'updated_id': id,
            'components': dictionary_components,
            'total_components': len(selection_components)
        })
    except Exception as e:
        print(e)
        if error_404:
            abort(404)
        elif error_422:
            abort(422)
        elif error_401:
            abort(401)
        elif error_403:
            abort(403)
        else:
            abort(500)


@api.route('/components', methods=['POST'])
def post_component():
    error_422 = False
    error_401 = False
    error_403 = False
    try:
        body = request.get_json()

        description = body.get('description', None)
        name = body.get('name', None)
        component_type = body.get('type', None)
        price = body.get('price', None)
        token = body.get('token', None)

        if description is None or name is None or component_type is None or price is None or token is None:
            error_422 = True
            abort(422)
        user = User.check_token(token)
        if user is None:
            error_401 = True
            abort(401)
        if user.role != 'admin':
            error_403 = True
            abort(403)
        create_by = user.id

        new_component = Component(
            description=description,
            name=name,
            component_type=component_type,
            price=price,
            create_by=create_by
        )
        new_component_id = new_component.insert()
        if new_component_id is None:
            error_422 = True
            abort(422)

        selection_components = Component.query.order_by('id').all()
        dictionary_components = {component.id: component.format() for component in selection_components}
        return jsonify({
            'success': True,
            'created_id': new_component_id,
            'components': dictionary_components,
            'total_components': len(selection_components)
        })
    except:
        if error_422:
            abort(422)
        elif error_401:
            abort(401)
        elif error_403:
            abort(403)
        else:
            abort(500)
