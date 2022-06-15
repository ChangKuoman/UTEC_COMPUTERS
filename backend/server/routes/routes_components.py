from flask import abort, jsonify, request
from models.Component import Component
from server.routes.__init__ import api


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
    name = body.get('name', None)
    component_type = body.get('type', None)
    price = body.get('price', None)
    create_by = body.get('create_by', None)

    search = body.get('search', None)
    components = body.get('components', None)

    if search:
        selection = []
        for value_searched in components:
            selection += Component.query.order_by('id').filter(Component.component_type == value_searched).all()
        list_components = {list.id: list.format() for list in selection}
        if len(selection) == 0:
            abort(404)

        return jsonify({
            'success': True,
            'components': list_components,
            'total_components': len(selection)
        })

    if description is None or name is None or component_type is None or price is None or create_by is None:
        abort(422)

    component = Component(
        description=description,
        name=name,
        component_type=component_type,
        price=price,
        create_by=create_by
    )
    new_component_id = component.insert()
    if new_component_id is None:
        abort(422)

    selection = Component.query.order_by('id').all()
    list_components = {list.id: list.format() for list in selection}

    return jsonify({
        'success': True,
        'created_id': new_component_id,
        'components': list_components,
        'total_components': len(selection)
    })


@api.route('/components/<id>', methods=['PATCH'])
def update_component(id):
    error_404 = False
    error_422 = False
    try:
        component_to_patch = Component.query.filter(Component.id==id).one_or_none()

        if component_to_patch is None:
            error_404 = True
            abort(404)

        body = request.get_json()

        if 'modify_by' not in body:
            error_422 = True
            abort(422)

        body = request.get_json()
        if 'description' in body:
            component_to_patch.description = body.get('description')
        if 'price' in body:
            component_to_patch.price = body.get('price')
        if 'type' in body:
            component_to_patch.component_type = body.get('type')
        if 'name' in body:
            component_to_patch.name = body.get('name')

        modify_by = body.get('modify_by')
        updated_id = component_to_patch.update(modify_by)
        if updated_id is None:
            error_422 = True
            abort(422)

        components_list = Component.query.order_by('id').all()
        components_dictionary = {component.id: component.format() for component in components_list}
        return jsonify({
            'success': True,
            'updated_id': id,
            'components': components_dictionary,
            'total_components': len(components_list)
        })
    except Exception as e:
        print(e)
        if error_404:
            abort(404)
        if error_422:
            abort(422)
        else:
            abort(500)


@api.route('/components/<id>', methods=['DELETE'])
def delete_component(id):
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
            'deleted_id': id,
            'components': lists_component,
            'total_components': len(selection)
        })

    except Exception as e:
        print(e)
        if error_404:
            abort(404)
        else:
            abort(500)


@api.route('/components/<id>', methods=['GET'])
def get_component(id):
    component = Component.query.filter(Component.id==id).one_or_none()

    if component is None:
        abort(404)

    component_dictionary = component.format()
    components_list = Component.query.order_by('id').all()
    return jsonify({
        'success': True,
        'component': component_dictionary,
        'total_components': len(components_list)
    })