import unittest
from app import app
import json

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_plus(self):
        # Send GET request
        response = self.app.get('/plus/5/6')

        # Check if status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Print response data for debugging
        print("Response Data:", response.data.decode('utf-8'))

        # Check if response is in valid JSON format
        try:
            json_data = json.loads(response.data.decode('utf-8'))
        except json.JSONDecodeError:
            self.fail(f"Response is not valid JSON: {response.data.decode('utf-8')}")
        
        # Assert the 'plus' key in the JSON response
        self.assertEqual(json_data['plus'], 11)

    def test_plus_float(self):
        # Send GET request with float numbers
        response = self.app.get('/plus/8.4/4')

        # Check if status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Print response data for debugging
        print("Response Data:", response.data.decode('utf-8'))

        # Check if response is in valid JSON format
        try:
            json_data = json.loads(response.data.decode('utf-8'))
        except json.JSONDecodeError:
            self.fail(f"Response is not valid JSON: {response.data.decode('utf-8')}")
        
        # Assert the 'plus' key in the JSON response
        self.assertEqual(json_data['plus'], 12.4)

if __name__ == '__main__':
    unittest.main()
