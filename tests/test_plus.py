import unittest
from app import app
import json

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_plus(self):
        print("Requesting /plus/5/6")
        response = self.app.get('/plus/5/6')

        # Check status code
        print("Response Status Code:", response.status_code)
        self.assertEqual(response.status_code, 200)

        # Print response data
        print("Response Data:", response.data.decode('utf-8'))

        # Decode response
        json_data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(json_data['plus'], 11)

    def test_plus_float(self):
        print("Requesting /plus/8.4/4")
        response = self.app.get('/plus/8.4/4')

        # Check status code
        print("Response Status Code:", response.status_code)
        self.assertEqual(response.status_code, 200)

        # Print response data
        print("Response Data:", response.data.decode('utf-8'))

        # Decode response
        json_data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(json_data['plus'], 12.4)

if __name__ == '__main__':
    unittest.main()
