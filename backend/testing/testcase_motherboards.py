import unittest
import sys
sys.path.append("..")
sys.path.append("../server")
from server import create_app
from config import setup_db
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
        res = self.client().post('/users', json = {
            'username': 'test-motherboard',
            'password': 'aA.12345',
            'role': 'admin'
        })
        data = json.loads(res.data)
        self.user_token = data['user']['token']
        self.user_id = data['user']['id']
        self.id = None


    def test_post_motherboard_success(self):
        new_motherboard = {
            'name': 'test-motherboard',
            'price': 20.00,
            'description': 'interesting',
            'token': self.user_token
        }
        res = self.client().post('/motherboards', json=new_motherboard)
        data = json.loads(res.data)
        self.id = data['created_id']

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(data['total_motherboards'])
        self.assertTrue(len(data['motherboards']))


    def test_post_motherboard_fail(self):
        new_motherboard = {
            'name': 'test-motherboard',
            'price': 20.00,
            'description': 'interesting'
        }
        res = self.client().post('/motherboards', json=new_motherboard)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'Unprocessable')
        self.assertTrue(data['code'], 422)


    def test_get_motherboards_success(self):
        motherboard = {
            'name': 'test-motherboard',
            'price': 20.00,
            'description': 'interesting',
            'token': self.user_token
        }
        res_motherboard = self.client().post('/motherboards', json=motherboard)
        data_motherboard = json.loads(res_motherboard.data)
        self.id = data_motherboard['created_id']

        res = self.client().get('/motherboards')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(data['total_motherboards'])
        self.assertTrue(len(data['motherboards']))


    def test_get_motherboard_success(self):
        motherboard = {
            'name': 'test-motherboard',
            'price': 20.00,
            'description': 'interesting',
            'token': self.user_token
        }
        motherboard_res = self.client().post('/motherboards', json=motherboard)
        motherboard_data = json.loads(motherboard_res.data)
        self.id = motherboard_data['created_id']

        res = self.client().get('/motherboards/' + str(motherboard_data['created_id']))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(data['total_motherboards'])
        self.assertTrue(data['motherboard'])
        self.assertEqual(data['motherboard']['name'], 'test-motherboard')


    def test_get_motherboard_fail(self):
        res = self.client().get('/motherboards/0')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'Resource Not Found')


    def test_delete_motherboard_success(self):
        motherboard = {
            'name': 'test-motherboard',
            'price': 20.00,
            'description': 'interesting',
            'token': self.user_token
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
        motherboard = {
            'name': 'test-motherboard',
            'price': 20.00,
            'description': 'interesting',
            'token': self.user_token
        }
        motherboard_res = self.client().post('/motherboards', json=motherboard)
        motherboard_data = json.loads(motherboard_res.data)
        self.id = motherboard_data['created_id']
        new_data = {
            'token': self.user_token,
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
        motherboard = {
            'name': 'test-motherboard',
            'price': 20.00,
            'description': 'interesting',
            'token': self.user_token
        }
        motherboard_res = self.client().post('/motherboards', json=motherboard)
        motherboard_data = json.loads(motherboard_res.data)
        self.id = motherboard_data['created_id']
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
        if self.id is not None:
            self.client().delete('/motherboards/' + str(self.id))
        self.client().delete('/users/' + str(self.user_id))

