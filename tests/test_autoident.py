# tests/test_autoident.py
from utils.base_test import BaseTest

class TestAutoident(BaseTest):
    def test_autoident_browser_support(self):
        """Test to validate the autoident key's browser support matrix."""
        response = self.get(self.base_url)

        autoident = response.get('settings', {}).get('idnow', {}).get('autoident', {})
        self.assertIsNotNone(autoident, "autoident key is missing")
        if not autoident:
            self.fail("The 'autoident' key is missing or empty in the response.")

        browser_support_matrix = autoident.get('web', {}).get('browserSupportMatrix', {})
        self.assertIsNotNone(browser_support_matrix, "browserSupportMatrix key is missing")
        print(type(browser_support_matrix))
        if self.check_min_key_exists(browser_support_matrix):
            print("'min' key exists for every browser.")
        else:
            print("'min' key does not exist for every browser.")
