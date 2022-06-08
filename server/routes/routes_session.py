from server.routes.__init__ import route

@route.route('/login', methods=['GET'])
def login():
    return {
        'success': "hola"
    }
