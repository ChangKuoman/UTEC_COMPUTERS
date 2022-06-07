from flask import abort, jsonify
from models.Simulation import Simulation
from RESTful_api.routes.__init__ import route

@route.route('/simulations', methods=['GET'])
def get_simulations():
    motherboards = Simulation.query.order_by('id').all()

    if len(motherboards) == 0:
        abort(404)

    formatted_motherboards = {motherboard.id: motherboard.format() for motherboard in motherboards}
    return jsonify({
        'success': True,
        'motherboards': formatted_motherboards,
        'total_motherboards': len(motherboards)
    })