from flask import abort, jsonify, request
from models.Compatible import Compatible
from server.routes.__init__ import api


@api.route('/compatibles', methods=['GET'])
def get_compatibles():
    selection_compatibles = Compatible.query.order_by('id').all()

    if len(selection_compatibles) == 0:
        abort(404)

    dictionary_compatibles = {compatible.id: compatible.format() for compatible in selection_compatibles}
    return jsonify({
        'success': True,
        'compatibles': dictionary_compatibles,
        'total_compatibles': len(selection_compatibles)
    })


@api.route('/compatibles/<id>', methods=['GET'])
def get_compatible(id):
    compatible = Compatible.query.filter(Compatible.id==id).one_or_none()

    if compatible is None:
        abort(404)

    dictionary_compatible = compatible.format()
    selection_compatibles = Compatible.query.order_by('id').all()
    return jsonify({
        'success': True,
        'compatible': dictionary_compatible,
        'total_compatibles': len(selection_compatibles)
    })


@api.route('/compatibles/<id>', methods=['DELETE'])
def delete_compatible(id):
    error_404 = False
    try:
        compatible_to_delete = Compatible.query.filter(Compatible.id==id).one_or_none()

        if compatible_to_delete is None:
            error_404 = True
            abort(404)

        compatible_to_delete.delete()

        selection_compatibles = Compatible.query.order_by('id').all()
        dictionary_compatibles = {compatible.id: compatible.format() for compatible in selection_compatibles}
        return jsonify({
            'success': True,
            'deleted_id': id,
            'compatibles': dictionary_compatibles,
            'total_componets': len(selection_compatibles)
        })
    except Exception as e:
        print(e)
        if error_404:
            abort(404)
        else:
            abort(500)


@api.route('/compatibles', methods=['POST'])
def post_compatible():
    error_422 = False
    try:
        body = request.get_json()

        id_motherboard = body.get('id_motherboard', None)
        id_component = body.get('id_component', None)
        create_by = body.get('create_by', None)

        if create_by is None or id_component is None or id_motherboard is None:
            error_422 = True
            abort(422)

        new_compatible = Compatible(create_by=create_by, id_component=id_component, id_motherboard=id_motherboard)
        new_compatible_id = new_compatible.insert()
        if new_compatible_id is None:
            error_422 = True
            abort(422)

        selection_compatibles = Compatible.query.order_by('id').all()
        dictionary_compatibles = {compatible.id: compatible.format() for compatible in selection_compatibles}
        return jsonify({
            'success': True,
            'created_id': new_compatible_id,
            'compatibles': dictionary_compatibles,
            'total_compatibles': len(selection_compatibles)
        })
    except:
        if error_422:
            abort(422)
        else:
            abort(500)
