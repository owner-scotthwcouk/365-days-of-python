import unittest
import os
import sys

class TestMonth7Week2(unittest.TestCase):
    def setUp(self):
        # Dynamically add the Week 2 folder to the system path
        self.week2_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../Week_2'))
        sys.path.insert(0, self.week2_path)

    def tearDown(self):
        if self.week2_path in sys.path:
            sys.path.remove(self.week2_path)

    def test_day180_render_template(self):
        """Test Day 180: Rendering HTML"""
        try:
            from day180 import app
            app.config['TESTING'] = True
            client = app.test_client()
            response = client.get('/')
            self.assertEqual(response.status_code, 200, "Day 180 Failed: Route did not return a 200 OK.")
            self.assertIn(b"<html", response.data.lower(), "Day 180 Failed: The route did not render an HTML document.")
        except ImportError:
            self.skipTest("day180.py not found.")

    def test_day181_template_variables(self):
        """Test Day 181: Passing Variables"""
        try:
            from day181 import app
            client = app.test_client()
            response = client.get('/profile')
            self.assertIn(b"Guido", response.data, "Day 181 Failed: The variable 'Guido' was not rendered into the HTML template.")
        except ImportError:
            self.skipTest("day181.py not found.")

    def test_day182_jinja_if_statements(self):
        """Test Day 182: Conditional HTML"""
        try:
            from day182 import app
            client = app.test_client()
            response = client.get('/')
            # Assuming the test script toggles login state
            self.assertTrue(b"Welcome" in response.data or b"Please log in" in response.data, 
                            "Day 182 Failed: Your Jinja2 if/else block did not render correctly.")
        except ImportError:
            self.skipTest("day182.py not found.")

    def test_day183_jinja_loops(self):
        """Test Day 183: Looping HTML Elements"""
        try:
            from day183 import app
            client = app.test_client()
            response = client.get('/items')
            self.assertIn(b"<li>", response.data, "Day 183 Failed: Your Jinja2 loop did not generate <li> tags.")
        except ImportError:
            self.skipTest("day183.py not found.")

    def test_day186_capstone_dynamic_page(self):
        """Test Day 186: The Templates Capstone"""
        try:
            from day186 import app
            client = app.test_client()
            response = client.get('/portfolio')
            
            # Check for inherited layout, static files, and looped data
            self.assertIn(b"stylesheet", response.data, "Day 186 Failed: Missing static CSS link.")
            self.assertIn(b"Project", response.data, "Day 186 Failed: Project data was not looped and rendered.")
            self.assertEqual(response.status_code, 200, "Day 186 Failed: The capstone route crashed.")
            
        except ImportError:
            self.skipTest("day186.py not found.")

if __name__ == '__main__':
    unittest.main()