from flask import abort, jsonify, request
from models.MotherBoard import MotherBoard
from server.routes.__init__ import api


@api.route('/motherboards', methods=['GET'])
def get_motherboards():
    motherboards_list = MotherBoard.query.order_by('id').all()

    if len(motherboards_list) == 0:
        abort(404)

    motherboards_dictionary = {motherboard.id: motherboard.format() for motherboard in motherboards_list}
    return jsonify({
        'success': True,
        'motherboards': motherboards_dictionary,
        'total_motherboards': len(motherboards_list)
    })


@api.route('/motherboards/<id>', methods=['GET'])
def get_motherboard(id):
    motherboard = MotherBoard.query.filter(MotherBoard.id==id).one_or_none()

    if motherboard is None:
        abort(404)

    motherboard_dictionary = motherboard.format()
    motherboards_list = MotherBoard.query.order_by('id').all()
    return jsonify({
        'success': True,
        'motherboard': motherboard_dictionary,
        'total_motherboards': len(motherboards_list)
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

        motherboards_list = MotherBoard.query.order_by('id').all()
        motherboards_dictionary = {motherboard.id: motherboard.format() for motherboard in motherboards_list}
        return jsonify({
            'success': True,
            'deleted_id': id,
            'motherboards': motherboards_dictionary,
            'total_motherboards': len(motherboards_list)
        })

    except Exception as e:
        print(e)
        if error_404:
            abort(404)
        else:
            abort(500)


@api.route('/motherboards', methods=['POST'])
def post_motherboard():
    error_422 = False
    try:
        body = request.get_json()

        price = body.get('price', None)
        name = body.get('name', None)
        description = body.get('description', None)
        create_by = body.get('create_by', None)

        if price is None or name is None or description is None or create_by is None:
            error_422 = True
            abort(422)

        new_motherboard = MotherBoard(price=price, name=name, description=description, create_by=create_by)
        new_motherboard_id = new_motherboard.insert()
        if new_motherboard_id is None:
            error_422 = True
            abort(422)

        motherboards_list = MotherBoard.query.order_by('id').all()
        motherboards_dictionary = {motherboard.id: motherboard.format() for motherboard in motherboards_list}
        return jsonify({
            'success': True,
            'created_id': new_motherboard_id,
            'motherboards': motherboards_dictionary,
            'total_motherboards': len(motherboards_list)
        })
    except:
        if error_422:
            abort(422)
        else:
            abort(500)





@api.route('/motherboards/<id>', methods=['PATCH'])
def patch_motherboard(id):
    error_404 = False
    error_422 = False
    try:
        motherboard_to_patch = MotherBoard.query.filter(MotherBoard.id==id).one_or_none()

        if motherboard_to_patch is None:
            error_404 = True
            abort(404)

        body = request.get_json()
        if 'modify_by' not in body:
            error_422 = True
            abort(422)

        if 'description' in body:
            motherboard_to_patch.description = body.get('description')
        if 'price' in body:
            motherboard_to_patch.price = body.get('price')
        if 'name' in body:
            motherboard_to_patch.description = body.get('name')

        modify_by = body.get('modify_by')
        motherboard_to_patch.update(modify_by)

        motherboards_list = MotherBoard.query.order_by('id').all()
        motherboards_dictionary = {motherboard.id: motherboard.format() for motherboard in motherboards_list}
        return jsonify({
            'success': True,
            'updated_id': id,
            'motherboards': motherboards_dictionary,
            'total_motherboards': len(motherboards_list)
        })
    except Exception as e:
        print(e)
        if error_404:
            abort(404)
        elif error_422:
            abort(422)
        else:
            abort(500)
