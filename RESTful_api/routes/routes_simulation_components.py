from flask import abort, jsonify
from models.SimulationComponent import SimulationComponent
from RESTful_api.routes.__init__ import route


@route.route('/simulationComponents', methods=['GET'])
def get_simulation_components():
    motherboards = SimulationComponent.query.order_by('id_simulation').all()

    if len(motherboards) == 0:
        abort(404)

    formatted_motherboards = {motherboard.id_simulation: [] for motherboard in motherboards}
    for  motherboard in motherboards:
        formatted_motherboards[motherboard.id_simulation].append(motherboard.format())

    return jsonify({
        'success': True,
        'motherboards': formatted_motherboards,
        'total_motherboards': len(motherboards)
    })
