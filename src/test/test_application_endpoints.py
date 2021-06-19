import unittest
import json
from src.test.base import BaseTestCase 
from src.test.api_callers.application_caller import application_form, application_form_field_based

class TestApplicationForm(BaseTestCase):

    def test_application_form(self):
        """ Test for mock response received for application form complete"""
        with self.client:
            api_response = application_form(self)
            response_data = json.loads(api_response.data.decode())

            self.assertTrue(response_data['status'] == "prediction completed")
            self.assertEqual(api_response.status_code, 200)

    def test_application_form_field_quantity(self):
        """ Test for mock response received for application form on quantity field"""
        with self.client:
            api_response = application_form_field_based(self, "quantity")
            response_data = json.loads(api_response.data.decode())

            self.assertTrue(response_data['status'] == "prediction for quantity completed")
            self.assertEqual(api_response.status_code, 200)

    def test_application_form_field_product(self):
        """ Test for mock response received for application form on product field"""
        with self.client:
            api_response = application_form_field_based(self, "product")
            response_data = json.loads(api_response.data.decode())

            self.assertTrue(response_data['status'] == "prediction for product completed")
            self.assertEqual(api_response.status_code, 200)

    def test_application_form_field_dose(self):
        """ Test for mock response received for application form on dose field"""
        with self.client:
            api_response = application_form_field_based(self, "dose")
            response_data = json.loads(api_response.data.decode())

            self.assertTrue(response_data['status'] == "prediction for dose completed")
            self.assertEqual(api_response.status_code, 200)

    def test_application_form_field_machine(self):
        """ Test for mock response received for application form on machine field"""
        with self.client:
            api_response = application_form_field_based(self, "machine")
            response_data = json.loads(api_response.data.decode())

            self.assertTrue(response_data['status'] == "prediction for machine completed")
            self.assertEqual(api_response.status_code, 200)
    

if __name__ == '__main__':
    unittest.main()
