import unittest
import json
from src.test.base import BaseTestCase
from src.test.api_callers.issue_caller import issue_form, issue_form_field_based

class TestIssueForm(BaseTestCase): 

    def test_issue_form(self):
        """ Test for mock response received for issue form complete"""
        with self.client:
            api_response = issue_form(self)
            response_data = json.loads(api_response.data.decode())

            self.assertTrue(response_data['status'] == "prediction completed")
            self.assertEqual(api_response.status_code, 200)

    def test_issue_form_field_description(self):
        """ Test for mock response received for issue form on description field"""
        with self.client:
            api_response = issue_form_field_based(self, "description")
            response_data = json.loads(api_response.data.decode())

            self.assertTrue(response_data['status'] == "prediction for description completed")
            self.assertEqual(api_response.status_code, 200)

    def test_issue_form_field_type(self):
        """ Test for mock response received for issue form on type field"""
        with self.client:
            api_response = issue_form_field_based(self, "type")
            response_data = json.loads(api_response.data.decode())

            self.assertTrue(response_data['status'] == "prediction for type completed")
            self.assertEqual(api_response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
