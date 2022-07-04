import unittest
import sys
sys.path.append("..")
sys.path.append("../server")
from server import create_app
from config import setup_db
import json
import configparser

class TestCaseUsers(unittest.TestCase):
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


    def test_post_user_success(self):
        new_user = {
            'username': 'test-user',
            'password': 'aA.12345'
        }
        res = self.client().post('/users', json=new_user)
        data = json.loads(res.data)
        self.id = data['created_id']

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['created_id'])
        self.assertTrue(data['total_users'])
        self.assertTrue(len(data['users']))


    def test_post_admin_success(self):
        new_user = {
            'username': 'test-user',
            'password': 'aA.12345',
            'role': 'admin'
        }
        res = self.client().post('/users', json=new_user)
        data = json.loads(res.data)
        self.id = data['created_id']

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['created_id'])
        self.assertTrue(data['total_users'])
        self.assertTrue(len(data['users']))


    def test_post_user_fail(self):
        new_user = {
            'username': 'test-user'
        }
        res = self.client().post('/users', json=new_user)
        data = json.loads(res.data)
        self.id = None

        self.assertEqual(res.status_code, 422)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'Unprocessable')
        self.assertEqual(data['code'], 422)


    def test_post_login_success(self):
        new_user = {
            'username': 'test-user',
            'password': 'aA.12345'
        }
        res_user = self.client().post('/users', json=new_user)
        data_user = json.loads(res_user.data)
        self.id = data_user['created_id']
        login_data = {
            'login': True,
            'username': 'test-user',
            'password': 'aA.12345'
        }
        res = self.client().post('/users', json=login_data)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(data['user'])
        self.assertTrue(data['token'])


    def test_post_login_fail(self):
        new_user = {
            'username': 'test-user',
            'password': 'aA.12345'
        }
        res_user = self.client().post('/users', json=new_user)
        data_user = json.loads(res_user.data)
        self.id = data_user['created_id']
        login_data = {
            'login': True,
            'username': 'test-user',
            'password': 'clave-incorrecta'
        }
        res = self.client().post('/users', json=login_data)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'Unprocessable')
        self.assertEqual(data['code'], 422)


    def test_get_users_success(self):
        new_user = {
            'username': 'test-user',
            'password': 'aA.12345'
        }
        res_user = self.client().post('/users', json=new_user)
        data_user = json.loads(res_user.data)
        self.id = data_user['created_id']

        res = self.client().get('/users')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(data['total_users'])
        self.assertTrue(len(data['users']))


    def test_patch_user_success(self):
        user = {
            'username': 'test-user',
            'password': 'aA.12345'
        }
        user_res = self.client().post('/users', json=user)
        user_data = json.loads(user_res.data)
        self.id = user_data['created_id']
        new_data = {
            'old_password': 'aA.12345',
            'new_password': 'aA.123456'
        }
        res = self.client().patch(
            '/users/' + str(user_data['created_id']),
            json = new_data
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(data['updated_id'])


    def test_patch_user_fail(self):
        user = {
            'username': 'Panqueque',
            'password': 'aA.12345'
        }
        user_res = self.client().post('/users', json=user)
        user_data = json.loads(user_res.data)
        self.id = user_data['created_id']
        new_data = {
            'old_password': 'somepassword',
            'new_password': 'aA.123456'
        }
        res = self.client().patch(
            '/users/' + str(user_data['created_id']),
            json = new_data
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertFalse(data['success'])
        self.assertEqual(data['code'], 422)
        self.assertEqual(data['message'], 'Unprocessable')


    def test_delete_user_success(self):
        user = {
            'username': 'username',
            'password': 'aA.12345'
        }
        user_res = self.client().post('/users', json=user)
        user_data = json.loads(user_res.data)
        self.id = user_data['created_id']
        res = self.client().delete(
            '/users/' + str(user_data['created_id'])
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['deleted_id'], str(user_data['created_id']))
        self.assertTrue(data['success'])


    def test_delete_user_fail(self):
        res = self.client().delete('/users/0')
        self.id = None
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['code'], 404)
        self.assertEqual(data['message'], 'Resource Not Found')


    def tearDown(self):
        if self.id is not None:
            self.client().delete('/users/' + str(self.id))
