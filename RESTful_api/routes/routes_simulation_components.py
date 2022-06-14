from flask import abort, jsonify, request
from models.SimulationComponent import SimulationComponent
from RESTful_api.routes.__init__ import api


@api.route('/simulationComponents', methods=['GET'])
def get_simulation_components():
    simulations_components_list = SimulationComponent.query.order_by('id_simulation').all()

    if len(simulations_components_list) == 0:
        abort(404)

    simulations_components_dictionary = {component.id_simulation: [] for component in simulations_components_list}
    for component in simulations_components_list:
        simulations_components_dictionary[component.id_simulation].append(component.format())

    return jsonify({
        'success': True,
        'simulation_components': simulations_components_dictionary,
        'total_simulation_components': len(simulations_components_list)
    })
