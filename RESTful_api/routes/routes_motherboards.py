from flask import abort, jsonify, request
from models.MotherBoard import MotherBoard
from RESTful_api.routes.__init__ import route


@route.route('/motherboards', methods=['GET'])
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


@route.route('/motherboards/<id>', methods=['DELETE'])
def delete_motherboards(id):
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


@route.route('/motherboards', methods=['POST'])
def post_motherboards():
    body = request.get_json()

    price = body.get('price', None)
    name = body.get('name', None)
    description = body.get('description', None)
    create_by = body.get('create_by', None)

    if price is None or name is None or description is None or create_by is None:
        abort(422)

    # TODO: verificar unique name, retorna null
    # TODO: en user server_default = 'user'
    # TODO: en los modelos hacer server_default = 'current_timestamp'
    new_motherboard = MotherBoard(price=price, name=name, description=description, create_by=create_by, modify_by=create_by)
    new_motherboard_id = new_motherboard.id
    new_motherboard.insert()

    motherboards_list = MotherBoard.query.order_by('id').all()
    motherboards_dictionary = {motherboard.id: motherboard.format() for motherboard in motherboards_list}
    return jsonify({
        'success': True,
        'created_id': new_motherboard_id,
        'motherboards': motherboards_dictionary,
        'total_motherboards': len(motherboards_list)
    })


@route.route('/todos/<todo_id>', methods=['PATCH'])
def update_todo(todo_id):
    error_404 = False
    try:
        todo = MotherBoard.query.filter(MotherBoard.id==todo_id).one_or_none()

        if todo is None:
            error_404 = True
            abort(404)
        
        body = request.get_json()
        if 'description' in body:
            todo.description = body.get('description')
        
        todo.update()

        return jsonify({
            'success': True,
            'id': todo_id
        })
    except Exception as e:
        print(e)
        if error_404:
            abort(404)
        else:
            abort(500)
