import unittest
import json
from src.test.base import BaseTestCase
from src.test.api_callers.sowing_caller import sowing_form, sowing_form_field_based

class TestSowingForm(BaseTestCase):

    def test_sowing_form(self):
        """ Test for mock response received for sowing form complete """
        with self.client:
            # user registration
            api_response = sowing_form(self)
            response_data = json.loads(api_response.data.decode())

            # here we can make asserts in order to prove we got the right response
            self.assertTrue(response_data['status'] == "prediction completed")
            self.assertEqual(api_response.status_code, 200)

    def test_sowing_form_field_quantity(self):
        """ Test for mock response received for sowing form on quantity field"""
        with self.client:
            # user registration
            api_response = sowing_form_field_based(self, "quantity")
            response_data = json.loads(api_response.data.decode())

            # here we can make asserts in order to prove we got the right response
            self.assertTrue(response_data['status'] == "prediction for quantity completed")
            self.assertEqual(api_response.status_code, 200)

    def test_sowing_form_field_harvest_duration(self):
        """ Test for mock response received for sowing form on harvest_duration field"""
        with self.client:
            # user registration
            api_response = sowing_form_field_based(self, "harvest_duration")
            response_data = json.loads(api_response.data.decode())

            # here we can make asserts in order to prove we got the right response
            self.assertTrue(response_data['status'] == "prediction for harvest_duration completed")
            self.assertEqual(api_response.status_code, 200)

    def test_sowing_form_field_time_to_harvest(self):
        """ Test for mock response received for sowing form on time_to_harvest field"""
        with self.client:
            # user registration
            api_response = sowing_form_field_based(self, "time_to_harvest")
            response_data = json.loads(api_response.data.decode())

            # here we can make asserts in order to prove we got the right response
            self.assertTrue(response_data['status'] == "prediction for time_to_harvest completed")
            self.assertEqual(api_response.status_code, 200)

    def test_sowing_form_field_crop(self):
        """ Test for mock response received for sowing form on crop field"""
        with self.client:
            # user registration
            api_response = sowing_form_field_based(self, "crop")
            response_data = json.loads(api_response.data.decode())

            # here we can make asserts in order to prove we got the right response
            self.assertTrue(response_data['status'] == "prediction for crop completed")
            self.assertEqual(api_response.status_code, 200)
    
    def test_sowing_form_field_expected_yield(self):
        """ Test for mock response received for sowing form on expected_yield field"""
        with self.client:
            # user registration
            api_response = sowing_form_field_based(self, "expected_yield")
            response_data = json.loads(api_response.data.decode())

            # here we can make asserts in order to prove we got the right response
            self.assertTrue(response_data['status'] == "prediction for expected_yield completed")
            self.assertEqual(api_response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
