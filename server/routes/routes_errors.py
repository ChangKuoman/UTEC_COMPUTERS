from server.routes.__init__ import route

@route.errorhandler(404)
def error_404(error):
    return {
        'success': False
    }, 404
