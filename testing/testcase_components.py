import unittest
import sys
sys.path.append("..")
sys.path.append("../backend")
from backend.server import create_app
from backend.config import setup_db
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

    def test_post_component_success(self):
        user = {
            'username': 'tpcs',
            'password': 'aA.12345'
        }
        user_res = self.client().post('/users', json=user)
        user_data = json.loads(user_res.data)

        component = {
            'name': 'c1',
            'price': 15.82,
            'description': 'interesting',
            'create_by': user_data['created_id'],
            'type': 'RAM'
        }
        res = self.client().post('/components', json=component)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(data['total_components'])
        self.assertTrue(len(data['components']))
        self.assertEqual(data['created_id'], data['created_id'])

    def test_post_component_fail(self):
        component = {
            'name': 'c2',
            'price': 15.82,
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
        user = {
            'username': 'tgcss',
            'password': 'aA.12345'
        }
        user_res = self.client().post('/users', json=user)
        user_data = json.loads(user_res.data)

        component = {
            'name': 'c3',
            'price': 15.82,
            'description': 'interesting',
            'create_by': user_data['created_id'],
            'type': 'RAM'
        }
        self.client().post('/components', json=component)

        res = self.client().get('/components')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(data['total_components'])
        self.assertTrue(len(data['components']))

    def test_get_component_success(self):
        user = {
            'username': 'tgcs',
            'password': 'aA.12345'
        }
        user_res = self.client().post('/users', json=user)
        user_data = json.loads(user_res.data)

        component = {
            'name': 'c4',
            'price': 15.82,
            'description': 'interesting',
            'create_by': user_data['created_id'],
            'type': 'RAM'
        }
        component_res = self.client().post('/components', json=component)
        component_data = json.loads(component_res.data)

        res = self.client().get('/components/' + str(component_data['created_id']))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(data['component'])
        self.assertTrue(data['total_components'])
        self.assertEqual(data['component']['name'], 'c4')

    def test_get_component_fail(self):
        res = self.client().get('/components/0')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['code'], 404)
        self.assertEqual(data['message'], 'Resource Not Found')

    def test_patch_component_success(self):
        user = {
            'username': 'tpatchcs',
            'password': 'aA.12345'
        }
        user_res = self.client().post('/users', json=user)
        user_data = json.loads(user_res.data)

        component = {
            'name': 'c5',
            'price': 15.82,
            'description': 'interesting',
            'create_by': user_data['created_id'],
            'type': 'RAM'
        }
        component_res = self.client().post('/components', json=component)
        component_data = json.loads(component_res.data)

        new_data = {
            'modify_by': user_data['created_id'],
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
        user = {
            'username': 'tpatchcf',
            'password': 'aA.12345'
        }
        user_res = self.client().post('/users', json=user)
        user_data = json.loads(user_res.data)

        component = {
            'name': 'c6',
            'price': 15.82,
            'description': 'interesting',
            'create_by': user_data['created_id'],
            'type': 'RAM'
        }
        component_res = self.client().post('/components', json=component)
        component_data = json.loads(component_res.data)

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
        user = {
            'username': 'tdcs',
            'password': 'aA.12345'
        }
        user_res = self.client().post('/users', json=user)
        user_data = json.loads(user_res.data)

        component = {
            'name': 'c7',
            'price': 15.82,
            'description': 'interesting',
            'create_by': user_data['created_id'],
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
        pass
