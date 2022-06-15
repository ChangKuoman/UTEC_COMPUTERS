from flask import jsonify
from server.routes.__init__ import api


@api.app_errorhandler(404)
def error_404(error):
    return jsonify({
        'success': False,
        'code': 404,
        'message': 'Resource Not Found'
    }), 404


@api.app_errorhandler(500)
def error_500(error):
    return jsonify({
        'success': False,
        'code': 500,
        'message': 'Internal Server Error'
    }), 500


@api.app_errorhandler(422)
def error_422(error):
    return jsonify({
        'success': False,
        'code': 422,
        'message': 'Unprocessable'
    }), 422
