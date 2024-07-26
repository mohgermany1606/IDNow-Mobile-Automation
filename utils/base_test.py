# utils/base_test.py
import requests
import unittest
from config.config import Config

class BaseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Setup for the test cases, including base URL."""
        cls.session = requests.Session()
        cls.base_url = Config.BASE_URL

    @classmethod
    def tearDownClass(cls):
        """Teardown for the test cases."""
        cls.session.close()

    def get(self, url, params=None):
        """Perform a GET request."""
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def post(self, url, data=None, json=None):
        """Perform a POST request."""
        response = self.session.post(url, data=data, json=json)
        response.raise_for_status()
        return response.json()

    def put(self, url, data=None, json=None):
        """Perform a PUT request."""
        response = self.session.put(url, data=data, json=json)
        response.raise_for_status()
        return response.json()

    def delete(self, url):
        """Perform a DELETE request."""
        response = self.session.delete(url)
        response.raise_for_status()
        return response.json()

    def check_min_key_exists(self, browser_dict):
        def check_min_in_nested_dict(d):
            if isinstance(d, dict):
                for key, value in d.items():
                    if isinstance(value, dict):
                        # Check if 'min' key exists at the current level
                        if 'min' in value:
                            continue
                        # Recursively check deeper levels
                        else:
                            if not check_min_in_nested_dict(value):
                                return False
            return True

        # Start the check from the top level of the browser dictionary
        return check_min_in_nested_dict(browser_dict)
