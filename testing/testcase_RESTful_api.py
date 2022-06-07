import unittest
from RESTful_api import create_app
from testing.config import setup_db
import json

class TestCaseRESTfulapi(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        setup_db(self.app)

        self.new_user = {
            'id': 1,
            'username': 'pepito',
            'password': 'clave',
            'role': 'admin'
        }

        self.new_motherboard = {
            'id': 1,
            'price': 50.0,
            'name': 'm1',
            'description': 'very imteresting'
        }

    def test_get_motherboards_success(self):
        self.client().post('/users', json=self.new_user)
        self.client().post('/motherboards', json=self.new_motherboard)

        res = self.client().get('/motherboards')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_motherboard'])
        self.assertTrue(len(data['motherboard']))
    
    def test_update_todo_success(self):
        res0 = self.client().post('/todos', json=self.new_todo)
        data0 = json.loads(res0.data)
        updated_id = data0['created']

        res = self.client().patch('/todos/' + str(updated_id), json={'description': 'update description'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['id'], str(updated_id))

    def test_update_todo_failed(self):
        res = self.client().patch('/todos/10000', json={'description': 'update description'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_delete_todo_success(self):
        res0 = self.client().post('/todos', json=self.new_todo)
        data0 = json.loads(res0.data)
        deleted_id = data0['created']

        res = self.client().delete('/todos/' + str(deleted_id))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], str(deleted_id))
        self.assertTrue(len(data['todos']))
        self.assertTrue(data['total_todos'])
    
    def test_create_todo_success(self):
        res = self.client().post('/todos', json=self.new_todo)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['todos']))
        self.assertTrue(data['total_todos'])

    def tearDown(self):
        pass