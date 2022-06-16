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

    def test_post_compatible_success(self):
        pass

    def test_post_compatible_fail(self):
        pass

    def test_get_compatibles_success(self):
        pass

    def test_get_compatible_success(self):
        pass

    def test_get_compatible_fail(self):
        pass

    def test_delete_compatible_success(self):
        pass

    def test_delete_compatible_fail(self):
        pass

    def tearDown(self):
        pass
