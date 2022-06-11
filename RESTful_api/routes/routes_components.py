from flask import abort, jsonify, request
from models.Component import Component
from RESTful_api.routes.__init__ import api


@api.route('/components', methods=['GET'])
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


@api.route('/components', methods=['POST'])
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
            'components': list_components,
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


@api.route('/components/<id>', methods=['PATCH'])
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


@api.route('/components/<id>', methods=['DELETE'])
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