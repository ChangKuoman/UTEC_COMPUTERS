from flask import abort, jsonify, request
from models.Simulation import Simulation
from RESTful_api.routes.__init__ import api


@api.route('/simulations', methods=['POST'])
def post_simulations():
    body = request.get_json()

    id_motherboard = body.get('id_motherboard', None)
    total_price = body.get('total_price', None)
    create_by = body.get('create_by', None)
    print(id_motherboard, total_price, create_by)

    if id_motherboard is None or total_price is None or create_by is None:
        abort(422)

    simulation = Simulation(id_motherboard=id_motherboard, total_price=total_price, create_by=create_by)
    new_simulation_id = simulation.insert()
    print(new_simulation_id)
    if new_simulation_id is None:
        abort(422)

    simulations_list = Simulation.query.order_by('id').all()
    simulations_dictionary = {simulation.id: simulation.format() for simulation in simulations_list}
    return jsonify({
        'success': True,
        'created': new_simulation_id,
        'simulations': simulations_dictionary,
        'total_simulations': len(simulations_list)
    })


@api.route('/simulations', methods=['GET'])
def get_simulations():
    simulations_list = Simulation.query.order_by('id').all()

    if len(simulations_list) == 0:
        abort(404)

    simulations_dictionary = {simulation.id: simulation.format() for simulation in simulations_list}
    return jsonify({
        'success': True,
        'simulations': simulations_dictionary,
        'total_simulations': len(simulations_list)
    })


@api.route('/simulations/<id>', methods=['GET'])
def get_simulation(id):
    simulation = Simulation.query.filter(Simulation.id==id).one_or_none()

    if simulation is None:
        abort(404)

    simulations_list = Simulation.query.order_by('id').all()

    simulation_dictionary = {simulation.id: simulation.format()}
    return jsonify({
        'success': True,
        'simulations': simulation_dictionary,
        'total_simulations': len(simulations_list)
    })


@api.route('/simulations/<id>', methods=['DELETE'])
def delete_simulation(id):
    error_404 = False
    try:
        simulation_to_delete = Simulation.query.filter(Simulation.id==id).one_or_none()

        if simulation_to_delete is None:
            error_404 = True
            abort(404)

        simulation_to_delete.delete()

        simulations_list = Simulation.query.order_by('id').all()
        simulations_dictionary = {simulation.id: simulation.format() for simulation in simulations_list}
        return jsonify({
            'success': True,
            'deleted_id': id,
            'simulations': simulations_dictionary,
            'total_simulations': len(simulations_list)
        })

    except Exception as e:
        print(e)
        if error_404:
            abort(404)
        else:
            abort(500)