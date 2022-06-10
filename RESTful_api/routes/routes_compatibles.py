from flask import abort, jsonify, request
from models.Compatible import Compatible
from RESTful_api.routes.__init__ import api


@api.route('/compatible', methods=['GET'])
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


@api.route('/compatible', methods=['POST'])
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


@api.route('/compatible/<id>', methods=['PATCH'])
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


@api.route('/compatible/<id>', methods=['DELETE'])
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