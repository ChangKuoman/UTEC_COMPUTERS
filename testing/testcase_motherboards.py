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


    def test_post_motherboard_success(self):
        user = {
            'username': 'tpms',
            'password': 'aA.12345'
        }
        user_res = self.client().post('/users', json=user)
        user_data = json.loads(user_res.data)

        new_motherboard = {
            'name': 'm0',
            'price': 15.82,
            'description': 'interesting',
            'create_by': user_data['created_id']
        }
        res = self.client().post('/motherboards', json=new_motherboard)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(data['total_motherboards'])
        self.assertTrue(len(data['motherboards']))


    def test_post_motherboard_fail(self):
        new_motherboard = {
            'name': 'm0',
            'price': 15.82,
            'description': 'interesting'
        }
        res = self.client().post('/motherboards', json=new_motherboard)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'Unprocessable')
        self.assertTrue(data['code'], 422)


    def test_get_motherboards_success(self):
        user = {
            'username': 'tgms',
            'password': 'aA.12345'
        }
        user_res = self.client().post('/users', json=user)
        user_data = json.loads(user_res.data)

        motherboard = {
            'name': 'm1',
            'price': 15.82,
            'description': 'interesting',
            'create_by': user_data['created_id']
        }
        self.client().post('/motherboards', json=motherboard)

        res = self.client().get('/motherboards')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(data['total_motherboards'])
        self.assertTrue(len(data['motherboards']))


    def test_get_motherboard_success(self):
        user = {
            'username': 'tgoms',
            'password': 'aA.12345'
        }
        user_res = self.client().post('/users', json=user)
        user_data = json.loads(user_res.data)

        motherboard = {
            'name': 'm1',
            'price': 15.82,
            'description': 'interesting',
            'create_by': user_data['created_id']
        }
        motherboard_res = self.client().post('/motherboards', json=motherboard)
        motherboard_data = json.loads(motherboard_res.data)

        res = self.client().get('/motherboards/' + str(motherboard_data['created_id']))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(data['total_motherboards'])
        self.assertTrue(data['motherboard'])
        self.assertEqual(data['motherboard']['name'], 'm1')


    def test_get_motherboard_false(self):
        res = self.client().get('/motherboards/0')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'Resource Not Found')


    def test_delete_motherboard_success(self):
        user = {
            'username': 'tdms',
            'password': 'aA.12345'
        }
        user_res = self.client().post('/users', json=user)
        user_data = json.loads(user_res.data)

        motherboard = {
            'name': 'm3',
            'price': 15.82,
            'description': 'interesting',
            'create_by': user_data['created_id']
        }
        motherboard_res = self.client().post('/motherboards', json=motherboard)
        motherboard_data = json.loads(motherboard_res.data)

        res = self.client().delete('/motherboards/' + str(motherboard_data['created_id']))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['deleted_id'], str(motherboard_data['created_id']))


    def test_delete_motherboard_fail(self):
        res = self.client().delete('/motherboards/0')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['code'], 404)
        self.assertEqual(data['message'], 'Resource Not Found')


    def test_patch_motherboard_success(self):
        user = {
            'username': 'tpostms',
            'password': 'aA.12345'
        }
        user_res = self.client().post('/users', json=user)
        user_data = json.loads(user_res.data)

        motherboard = {
            'name': 'm4',
            'price': 15.82,
            'description': 'interesting',
            'create_by': user_data['created_id']
        }
        motherboard_res = self.client().post('/motherboards', json=motherboard)
        motherboard_data = json.loads(motherboard_res.data)

        new_data = {
            'modify_by': user_data['created_id'],
            'description': 'something'
        }
        res = self.client().patch(
            '/motherboards/' + str(motherboard_data['created_id']),
            json = new_data
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['updated_id'], str(motherboard_data['created_id']))
        self.assertTrue(len(data['motherboards']))
        self.assertTrue(data['total_motherboards'])


    def test_patch_motherboard_fail(self):
        user = {
            'username': 'tpostmf',
            'password': 'aA.12345'
        }
        user_res = self.client().post('/users', json=user)
        user_data = json.loads(user_res.data)

        motherboard = {
            'name': 'm5',
            'price': 15.82,
            'description': 'interesting',
            'create_by': user_data['created_id']
        }
        motherboard_res = self.client().post('/motherboards', json=motherboard)
        motherboard_data = json.loads(motherboard_res.data)

        new_data = {
            'description': 'something'
        }
        res = self.client().patch(
            '/motherboards/' + str(motherboard_data['created_id']),
            json = new_data
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertFalse(data['success'])
        self.assertEqual(data['code'], 422)
        self.assertEqual(data['message'], 'Unprocessable')


    def tearDown(self):
        pass
