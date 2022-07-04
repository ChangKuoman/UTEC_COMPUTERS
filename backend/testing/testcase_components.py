import unittest
import sys
sys.path.append("..")
sys.path.append("../server")
from server import create_app
from config import setup_db
import json
import configparser

class TestCaseComponents(unittest.TestCase):
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
        res = self.client().post('/users', json = {
            'username': 'test-component',
            'password': 'aA.12345',
            'role': 'admin'
        })
        data = json.loads(res.data)
        self.user_token = data['user']['token']
        self.user_id = data['user']['id']
        self.id = None


    def test_post_component_success(self):
        component = {
            'name': 'test-component',
            'price': 20.00,
            'description': 'interesting',
            'token': self.user_token,
            'type': 'RAM'
        }
        res = self.client().post('/components', json=component)
        data = json.loads(res.data)
        self.id = data['created_id']

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(data['total_components'])
        self.assertTrue(len(data['components']))


    def test_post_component_fail(self):
        component = {
            'name': 'test-component',
            'price': 20.00,
            'description': 'interesting',
            'type': 'RAM'
        }
        res = self.client().post('/components', json=component)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertFalse(data['success'])
        self.assertEqual(data['code'], 422)
        self.assertEqual(data['message'], 'Unprocessable')


    def test_get_components_success(self):
        component = {
            'name': 'test-component',
            'price': 20.00,
            'description': 'interesting',
            'token': self.user_token,
            'type': 'RAM'
        }
        res_component = self.client().post('/components', json=component)
        data_component = json.loads(res_component.data)
        self.id = data_component['created_id']

        res = self.client().get('/components')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(data['total_components'])
        self.assertTrue(len(data['components']))


    def test_get_component_success(self):
        component = {
            'name': 'test-component',
            'price': 20.00,
            'description': 'interesting',
            'token': self.user_token,
            'type': 'RAM'
        }
        component_res = self.client().post('/components', json=component)
        component_data = json.loads(component_res.data)
        self.id = component_data['created_id']
        res = self.client().get('/components/' + str(component_data['created_id']))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(data['component'])
        self.assertTrue(data['total_components'])
        self.assertEqual(data['component']['name'], 'test-component')


    def test_get_component_fail(self):
        res = self.client().get('/components/0')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['code'], 404)
        self.assertEqual(data['message'], 'Resource Not Found')


    def test_patch_component_success(self):
        component = {
            'name': 'test-component',
            'price': 20.00,
            'description': 'interesting',
            'token': self.user_token,
            'type': 'RAM'
        }
        component_res = self.client().post('/components', json=component)
        component_data = json.loads(component_res.data)
        self.id = component_data['created_id']
        new_data = {
            'token': self.user_token,
            'price': 20.25
        }
        res = self.client().patch(
            '/components/' + str(component_data['created_id']),
            json = new_data
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['updated_id'], str(component_data['created_id']))
        self.assertTrue(len(data['components']))
        self.assertTrue(data['total_components'])


    def test_patch_component_fail(self):
        component = {
            'name': 'test-component',
            'price': 20.00,
            'description': 'interesting',
            'token': self.user_token,
            'type': 'RAM'
        }
        component_res = self.client().post('/components', json=component)
        component_data = json.loads(component_res.data)
        self.id = component_data['created_id']
        new_data = {
            'price': 20.25
        }
        res = self.client().patch(
            '/components/' + str(component_data['created_id']),
            json = new_data
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertFalse(data['success'])
        self.assertEqual(data['code'], 422)
        self.assertEqual(data['message'], 'Unprocessable')


    def test_delete_component_success(self):
        component = {
            'name': 'test-component',
            'price': 20.00,
            'description': 'interesting',
            'token': self.user_token,
            'type': 'RAM'
        }
        component_res = self.client().post('/components', json=component)
        component_data = json.loads(component_res.data)

        res = self.client().delete(
            '/components/' + str(component_data['created_id'])
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['deleted_id'], str(component_data['created_id']))


    def test_delete_component_fail(self):
        res = self.client().delete(
            '/components/0'
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['code'], 404)
        self.assertEqual(data['message'], 'Resource Not Found')


    def tearDown(self):
        if self.id is not None:
            self.client().delete('/components/' + str(self.id))
        self.client().delete('/users/' + str(self.user_id))
