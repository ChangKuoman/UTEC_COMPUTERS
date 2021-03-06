from flask import abort, jsonify, request
from models.MotherBoard import MotherBoard
from server.routes.__init__ import api
from models.User import User


@api.route('/motherboards', methods=['GET'])
def get_motherboards():
    selection_motherboards = MotherBoard.query.order_by('id').all()

    if len(selection_motherboards) == 0:
        abort(404)

    dictionary_motherboards = {motherboard.id: motherboard.format() for motherboard in selection_motherboards}
    return jsonify({
        'success': True,
        'motherboards': dictionary_motherboards,
        'total_motherboards': len(selection_motherboards)
    })


@api.route('/motherboards/<id>', methods=['GET'])
def get_motherboard(id):
    motherboard = MotherBoard.query.filter(MotherBoard.id==id).one_or_none()

    if motherboard is None:
        abort(404)

    dictionary_motherboard = motherboard.format()
    selection_motherboards = MotherBoard.query.order_by('id').all()
    return jsonify({
        'success': True,
        'motherboard': dictionary_motherboard,
        'total_motherboards': len(selection_motherboards)
    })


@api.route('/motherboards/<id>', methods=['DELETE'])
def delete_motherboard(id):
    error_404 = False
    try:
        motherboard_to_delete = MotherBoard.query.filter(MotherBoard.id==id).one_or_none()

        if motherboard_to_delete is None:
            error_404 = True
            abort(404)

        motherboard_to_delete.delete()

        selection_motherboards = MotherBoard.query.order_by('id').all()
        dictionary_motherboards = {motherboard.id: motherboard.format() for motherboard in selection_motherboards}
        return jsonify({
            'success': True,
            'deleted_id': id,
            'motherboards': dictionary_motherboards,
            'total_motherboards': len(selection_motherboards)
        })
    except Exception as e:
        print(e)
        if error_404:
            abort(404)
        else:
            abort(500)


@api.route('/motherboards/<id>', methods=['PATCH'])
def patch_motherboard(id):
    error_404 = False
    error_422 = False
    error_401 = False
    error_403 = False
    try:
        motherboard_to_patch = MotherBoard.query.filter(MotherBoard.id==id).one_or_none()

        if motherboard_to_patch is None:
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

        motherboard_to_patch.modify_by = user.id
        if 'description' in body:
            motherboard_to_patch.description = body.get('description')
        if 'price' in body:
            motherboard_to_patch.price = body.get('price')
        if 'name' in body:
            motherboard_to_patch.name = body.get('name')

        updated_id = motherboard_to_patch.update()
        if updated_id is None:
            error_422 = True
            abort(422)

        selection_motherboards = MotherBoard.query.order_by('id').all()
        dictionary_motherboards = {motherboard.id: motherboard.format() for motherboard in selection_motherboards}
        return jsonify({
            'success': True,
            'updated_id': id,
            'motherboards': dictionary_motherboards,
            'total_motherboards': len(selection_motherboards)
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


@api.route('/motherboards', methods=['POST'])
def post_motherboard():
    error_422 = False
    error_401 = False
    error_403 = False
    try:
        body = request.get_json()

        price = body.get('price', None)
        name = body.get('name', None)
        description = body.get('description', None)
        token = body.get('token', None)

        if price is None or name is None or description is None or token is None:
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

        new_motherboard = MotherBoard(price=price, name=name, description=description, create_by=create_by)
        new_motherboard_id = new_motherboard.insert()
        if new_motherboard_id is None:
            error_422 = True
            abort(422)

        selection_motherboards = MotherBoard.query.order_by('id').all()
        dictionary_motherboards = {motherboard.id: motherboard.format() for motherboard in selection_motherboards}
        return jsonify({
            'success': True,
            'created_id': new_motherboard_id,
            'motherboards': dictionary_motherboards,
            'total_motherboards': len(selection_motherboards)
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
