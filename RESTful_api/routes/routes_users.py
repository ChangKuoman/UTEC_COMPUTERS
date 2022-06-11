from flask import abort, jsonify, request
from models.User import User
from RESTful_api.routes.__init__ import api


@api.route('/users', methods=['GET'])
def get_users():
    selection_users = User.query.order_by('id').all()

    if len(selection_users) == 0:
        abort(404)

    lists_users = {list.id: list.format() for list in selection_users}

    return jsonify({
        'success': True,
        'users': lists_users,
        'total_users': len(selection_users)
    })


@api.route('/users', methods=['POST'])
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


@api.route('/users/<id>', methods=['PATCH'])
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


@api.route('/users/<id>', methods=['DELETE'])
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