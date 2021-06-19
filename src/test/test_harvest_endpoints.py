import unittest
import json
from src.test.base import BaseTestCase
from src.test.api_callers.harvest_caller import harvest_form, harvest_form_field_based

class TestHarvestForm(BaseTestCase):

    def test_harvest_form(self):
        """ Test for mock response received for harvest form complete"""
        with self.client:
            api_response = harvest_form(self)
            response_data = json.loads(api_response.data.decode())

            self.assertTrue(response_data['status'] == "prediction completed")
            self.assertEqual(api_response.status_code, 200)

    def test_harvest_form_field_quantity(self):
        """ Test for mock response received for harvest form on quantity field"""
        with self.client:
            api_response = harvest_form_field_based(self, "quantity")
            response_data = json.loads(api_response.data.decode())

            self.assertTrue(response_data['status'] == "prediction for quantity completed")
            self.assertEqual(api_response.status_code, 200)

    def test_harvest_form_field_quantity_other_unit(self):
        """ Test for mock response received for harvest form on quantity other unit field"""
        with self.client:
            api_response = harvest_form_field_based(self, "quantity_other_unit")
            response_data = json.loads(api_response.data.decode())

            self.assertTrue(response_data['status'] == "prediction for quantity other unit completed")
            self.assertEqual(api_response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
