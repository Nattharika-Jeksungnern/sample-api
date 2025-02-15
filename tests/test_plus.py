import unittest
from app import app
import json

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_plus(self):
        response = self.app.get('/plus/5/6')
        
        # Convert the response to a JSON object
        json_data = json.loads(response.data.decode('utf-8'))
        
        # Assert that the 'plus' key contains the correct result
        self.assertEqual(json_data['plus'], 11)

    def test_plus_float(self):
        response = self.app.get('/plus/8.4/4')
        
        # Convert the response to a JSON object
        json_data = json.loads(response.data.decode('utf-8'))
        
        # Assert that the 'plus' key contains the correct result
        self.assertEqual(json_data['plus'], 12.4)

if __name__ == '__main__':
    unittest.main()
