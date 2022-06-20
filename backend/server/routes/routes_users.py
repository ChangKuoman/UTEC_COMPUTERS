from flask import abort, jsonify, request
from models.User import User
from server.routes.__init__ import api


@api.route('/users', methods=['GET'])
def get_users():
    selection_users = User.query.order_by('id').all()

    if len(selection_users) == 0:
        abort(404)

    dictionary_users = {user.id: user.format() for user in selection_users}
    return jsonify({
        'success': True,
        'users': dictionary_users,
        'total_users': len(selection_users)
    })


@api.route('/users/<id>', methods=['GET'])
def get_user(id):
    user = User.query.filter(User.id==id).one_or_none()

    if user is None:
        abort(404)

    dictionary_user = user.format()
    selection_users = User.query.order_by('id').all()
    return jsonify({
        'success': True,
        'users': dictionary_user,
        'total_users': len(selection_users)
    })


@api.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    error_404 = False
    try:
        user_to_delete = User.query.filter(User.id==id).one_or_none()

        if user_to_delete is None:
            error_404 = True
            abort(404)

        user_to_delete.delete()

        selection_users = User.query.order_by('id').all()
        dictionary_users = {user.id: user.format() for user in selection_users}
        return jsonify({
            'success': True,
            'deleted_id': id,
            'users': dictionary_users,
            'total_users': len(selection_users)
        })
    except Exception as e:
        print(e)
        if error_404:
            abort(404)
        else:
            abort(500)


@api.route('/users/<id>', methods=['PATCH'])
def patch_user(id):
    error_404 = False
    error_422 = False
    try:
        user_to_patch = User.query.filter(User.id==id).one_or_none()

        if user_to_patch is None:
            error_404 = True
            abort(404)

        body = request.get_json()
        old_password = body.get('old_password', None)
        new_password = body.get('new_password', None)

        if old_password is None or new_password is None:
            error_422 = True
            abort(422)

        if not user_to_patch.check_password(old_password):
            error_422 = True
            abort(422)

        user_to_patch.change_password(new_password)
        user_to_patch.update()

        selection_users = User.query.order_by('id').all()
        dictionary_users = {user.id: user.format() for user in selection_users}
        return jsonify({
            'success': True,
            'updated_id': id,
            'users': dictionary_users,
            'total_users': len(selection_users)
        })
    except Exception as e:
        print(e)
        if error_404:
            abort(404)
        elif error_422:
            abort(422)
        else:
            abort(500)


@api.route('/users', methods=['POST'])
def post_user():
    error_404 = False
    error_422 = False
    try:
        body = request.get_json()

        username = body.get('username', None)
        password = body.get('password', None)
        role = body.get('role', None)

        login = body.get('login', None)
        if login:
            user = User.query.filter(User.username==username).one_or_none()
            if user is None:
                error_404 = True
                abort(404)
            if not user.check_password(password):
                error_422 = True
                abort(422)

            key = user.generate_key()
            return jsonify({
                'success': True,
                'user': user.format(),
                'token': key
            })

        if username is None or password is None:
            error_422 = True
            abort(422)

        if role is None:
            new_user = User(username=username, password=password)
        else:
            new_user = User(username=username, password=password, role=role)

        new_user_id = new_user.insert()
        if new_user_id is None:
            error_422 = True
            abort(422)

        selection_users = User.query.order_by('id').all()
        dictionary_users = {user.id: user.format() for user in selection_users}
        return jsonify({
            'success': True,
            'created_id': new_user_id,
            'users': dictionary_users,
            'total_users': len(selection_users)
        })
    except:
        if error_404:
            abort(404)
        elif error_422:
            abort(422)
        else:
            abort(500)
