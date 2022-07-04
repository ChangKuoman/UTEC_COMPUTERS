from flask import abort, jsonify, request
from models.Simulation import Simulation
from models.SimulationComponent import SimulationComponent
from server.routes.__init__ import api
from models.User import User


@api.route('/simulations', methods=['GET'])
def get_simulations():
    selection_simulations = Simulation.query.order_by('id').all()

    if len(selection_simulations) == 0:
        abort(404)

    dictionary_simulations = {simulation.id: simulation.format() for simulation in selection_simulations}
    return jsonify({
        'success': True,
        'simulations': dictionary_simulations,
        'total_simulations': len(selection_simulations)
    })


@api.route('/simulations/<id>', methods=['GET'])
def get_simulation(id):
    simulation = Simulation.query.filter(Simulation.id==id).one_or_none()

    if simulation is None:
        abort(404)

    dictionary_simulation = simulation.format()
    selection_simulations = Simulation.query.order_by('id').all()
    return jsonify({
        'success': True,
        'simulation': dictionary_simulation,
        'total_simulations': len(selection_simulations)
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

        selection_simulations = Simulation.query.order_by('id').all()
        dictionary_simulations = {simulation.id: simulation.format() for simulation in selection_simulations}
        return jsonify({
            'success': True,
            'deleted_id': id,
            'simulations': dictionary_simulations,
            'total_simulations': len(selection_simulations)
        })
    except Exception as e:
        print(e)
        if error_404:
            abort(404)
        else:
            abort(500)


@api.route('/simulations', methods=['POST'])
def post_simulation():
    error_422 = False
    error_401 = True
    try:
        body = request.get_json()

        id_motherboard = body.get('id_motherboard', None)
        total_price = body.get('total_price', None)
        create_by = body.get('create_by', None)
        components_id = body.get('components_id', None)
        token = body.get('token', None)

        if id_motherboard is None or total_price is None or token is None:
            error_422 = True
            abort(422)

        user = User.check_token(token)
        if user is None:
            error_401 = True
            abort(401)
        create_by = user.id

        new_simulation = Simulation(id_motherboard=id_motherboard, total_price=total_price, create_by=create_by)
        new_simulation_id = new_simulation.insert()
        if new_simulation_id is None:
            error_422 = True
            abort(422)

        for id in components_id:
            simulation_component = SimulationComponent(id_simulation=new_simulation_id, id_component=id)
            simulation_component.insert()

        selection_simulations = Simulation.query.order_by('id').all()
        dictionary_simulations = {simulation.id: simulation.format() for simulation in selection_simulations}
        return jsonify({
            'success': True,
            'created_id': new_simulation_id,
            'simulations': dictionary_simulations,
            'total_simulations': len(selection_simulations)
        })
    except:
        if error_422:
            abort(422)
        if error_401:
            abort(401)
        else:
            abort(500)
