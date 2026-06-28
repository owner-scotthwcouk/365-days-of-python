import unittest
import os
import sys

class TestMonth7Week1(unittest.TestCase):
    def setUp(self):
        # Dynamically add the Week 1 folder to the system path so we can import the student's apps
        self.week1_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../Week_1'))
        sys.path.insert(0, self.week1_path)

    def tearDown(self):
        # Clean up the path after tests
        if self.week1_path in sys.path:
            sys.path.remove(self.week1_path)

    def test_day173_hello_route(self):
        """Test Day 173: Basic Flask Initialization and Routing"""
        try:
            from day173 import app
            app.config['TESTING'] = True
            client = app.test_client()
            response = client.get('/')
            self.assertEqual(response.status_code, 200, "Day 173 Failed: The route did not return a 200 OK status.")
            self.assertIn(b"Hello, Web!", response.data, "Day 173 Failed: The home route did not return the correct greeting.")
        except ImportError:
            self.skipTest("day173.py not found or app not defined correctly.")

    def test_day174_about_route(self):
        """Test Day 174: Adding Endpoints"""
        try:
            from day174 import app
            client = app.test_client()
            response = client.get('/about')
            self.assertEqual(response.status_code, 200, "Day 174 Failed: The /about route did not return a 200 OK status.")
            self.assertIn(b"Python web app", response.data, "Day 174 Failed: The /about route did not return the correct string.")
        except ImportError:
            self.skipTest("day174.py not found.")

    def test_day175_post_methods(self):
        """Test Day 175: HTTP Methods"""
        try:
            from day175 import app
            client = app.test_client()
            response = client.post('/submit')
            self.assertEqual(response.status_code, 200, "Day 175 Failed: The route rejected the POST request.")
            self.assertIn(b"Form submitted", response.data, "Day 175 Failed: The POST request did not return the correct string.")
        except ImportError:
            self.skipTest("day175.py not found.")

    def test_day176_dynamic_routing(self):
        """Test Day 176: Capturing URL Variables"""
        try:
            from day176 import app
            client = app.test_client()
            response = client.get('/user/Guido')
            self.assertIn(b"Guido", response.data, "Day 176 Failed: The dynamic route did not capture and return the URL variable.")
        except ImportError:
            self.skipTest("day176.py not found.")

    def test_day178_jsonify(self):
        """Test Day 178: Returning JSON"""
        try:
            from day178 import app
            client = app.test_client()
            response = client.get('/api/data')
            self.assertTrue(response.is_json, "Day 178 Failed: The response was not formatted as JSON.")
            self.assertEqual(response.get_json().get("language"), "Python", "Day 178 Failed: The JSON payload was missing or incorrect.")
        except ImportError:
            self.skipTest("day178.py not found.")

    def test_day179_capstone_portfolio(self):
        """Test Day 179: Multi-Route Capstone"""
        try:
            from day179 import app
            client = app.test_client()
            
            # Check all three routes
            res_home = client.get('/')
            res_user = client.get('/user/Test')
            res_api = client.get('/api/contact')
            
            self.assertEqual(res_home.status_code, 200, "Day 179 Failed: Home route missing.")
            self.assertIn(b"Test", res_user.data, "Day 179 Failed: Dynamic user route missing or broken.")
            self.assertTrue(res_api.is_json, "Day 179 Failed: API route did not return JSON.")
            
        except ImportError:
            self.skipTest("day179.py not found.")

if __name__ == '__main__':
    unittest.main()