import unittest
import sys
sys.path.append("..")
sys.path.append("../backend")
from backend.server import create_app
from backend.config import setup_db
import json
import configparser

class TestCaseMotherboards(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client

        parser = configparser.ConfigParser()
        parser.read("config.txt")
        username = parser.get("config", "username")
        password = parser.get("config", "password")
        host = parser.get("config", "host")
        database_name = parser.get("config", "database_name")
        self.database_path = f'postgresql://{username}:{password}@{host}/{database_name}'
        setup_db(self.app, self.database_path)

        user_res = self.client().post('/users', json = {
            'username': 'test-simulation',
            'password': 'aA.12345'
        })
        user_data = json.loads(user_res.data)
        self.user_id = user_data['created_id']

        motherboard_res = self.client().post('/motherboards', json = {
            'name': 'test-simulation-m',
            'price': 20.00,
            'description': 'interesting',
            'create_by': self.user_id
        })
        motherboard_data = json.loads(motherboard_res.data)
        self.motherboard_id = motherboard_data['created_id']

        component_res = self.client().post('/components', json = {
            'name': 'test-simulation-c',
            'price': 20.00,
            'description': 'interesting',
            'create_by': self.user_id,
            'type': 'RAM'
        })
        component_data = json.loads(component_res.data)
        self.component_id = component_data['created_id']

        self.id = None


    def test_post_simulation_without_components_success(self):
        simulation = {
            'id_motherboard': self.motherboard_id,
            'total_price': 20.00,
            'create_by': self.user_id,
            'components_id': []
        }
        res = self.client().post('/simulations', json = simulation)
        data = json.loads(res.data)
        self.id = data['created_id']

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(data['created_id'])
        self.assertTrue(data['total_simulations'])
        self.assertTrue(len(data['simulations']))


    def test_post_simulation_with_components_success(self):
        simulation = {
            'id_motherboard': self.motherboard_id,
            'total_price': 20.00,
            'create_by': self.user_id,
            'components_id': [self.component_id]
        }
        res = self.client().post('/simulations', json = simulation)
        data = json.loads(res.data)
        self.id = data['created_id']

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(data['created_id'])
        self.assertTrue(data['total_simulations'])
        self.assertTrue(len(data['simulations']))


    def test_post_simulation_fail(self):
        simulation = {
            'id_motherboard': self.motherboard_id,
            'total_price': 20.00,
            'components_id': []
        }
        res = self.client().post('/simulations', json = simulation)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertFalse(data['success'])
        self.assertEqual(data['code'], 422)
        self.assertEqual(data['message'], 'Unprocessable')


    def test_get_simulations_success(self):
        simulation = {
            'id_motherboard': self.motherboard_id,
            'total_price': 20.00,
            'create_by': self.user_id,
            'components_id': [self.component_id]
        }
        simulation_res = self.client().post('/simulations', json = simulation)
        simulation_data = json.loads(simulation_res.data)
        self.id = simulation_data['created_id']

        res = self.client().get('/simulations')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(data['total_simulations'])
        self.assertTrue(len(data['simulations']))


    def test_get_simulation_success(self):
        simulation = {
            'id_motherboard': self.motherboard_id,
            'total_price': 20.00,
            'create_by': self.user_id,
            'components_id': [self.component_id]
        }
        simulation_res = self.client().post('/simulations', json = simulation)
        simulation_data = json.loads(simulation_res.data)
        self.id = simulation_data['created_id']

        res = self.client().get('/simulations/' + str(simulation_data['created_id']))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(data['total_simulations'])
        self.assertTrue(data['simulation'])


    def test_get_simulation_fail(self):
        res = self.client().get('/simulations/0')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['code'], 404)
        self.assertEqual(data['message'], 'Resource Not Found')


    def test_delete_simulation_success(self):
        simulation = {
            'id_motherboard': self.motherboard_id,
            'total_price': 20.00,
            'create_by': self.user_id,
            'components_id': [self.component_id]
        }
        simulation_res = self.client().post('/simulations', json = simulation)
        simulation_data = json.loads(simulation_res.data)
        self.id = simulation_data['created_id']

        res = self.client().delete('/simulations/' + str(simulation_data['created_id']))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['deleted_id'], str(simulation_data['created_id']))


    def test_delete_simulation_fail(self):
        res = self.client().delete('/simulations/0')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['code'], 404)
        self.assertEqual(data['message'], 'Resource Not Found')


    def tearDown(self):
        if self.id is not None:
            self.client().delete('/simulations/' + str(self.id))
        self.client().delete('/components/' + str(self.component_id))
        self.client().delete('/motherboards/' + str(self.motherboard_id))
        self.client().delete('/users/' + str(self.user_id))