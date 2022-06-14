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
def create_user():
    body = request.get_json()

    username = body.get('username', None)
    password = body.get('password', None)
    password_confirm = body.get('password_confirm', None)
    login = body.get('login', None)
    if login:
        user = User.query.filter(User.username==username).one_or_none()
        if user is None:
            abort(404)
        if not user.check_password(password):
            abort(422)

        key = user.generate_key()
        return jsonify({
            'success': True,
            'user': user.format(),
            'token': key
        })

    if username is None or password is None or password_confirm is None:
        abort(422)

    if password != password_confirm:
        abort(422)

    user = User(username=username, password=password)
    new_user_id = user.insert()
    if new_user_id is None:
        abort(422)

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
    error_422 = False
    try:
        user = User.query.filter(User.id==id).one_or_none()

        if user is None:
            error_404 = True
            abort(404)

        body = request.get_json()
        old_password = body.get('old_password', None)
        new_password = body.get('new_password', None)

        if old_password is None or new_password is None:
            abort(422)

        value = user.change_password(old_password, new_password)
        if value == False:
            error_422 = True
            abort(422)

        user.update()

        return jsonify({
            'success': True,
            'id': user.id
        })

    except Exception as e:
        print(e)
        if error_404:
            abort(404)
        elif error_422:
            abort(422)
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