import unittest
import os
import sys

class TestMonth7Week3(unittest.TestCase):
    def setUp(self):
        # Dynamically add the Week 3 folder to the system path
        self.week3_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../Week_3'))
        sys.path.insert(0, self.week3_path)

    def tearDown(self):
        if self.week3_path in sys.path:
            sys.path.remove(self.week3_path)

    def test_day187_post_methods(self):
        """Test Day 187: Handling POST requests"""
        try:
            from day187 import app
            app.config['TESTING'] = True
            client = app.test_client()
            response = client.post('/submit')
            self.assertEqual(response.status_code, 200, "Day 187 Failed: The route rejected the POST request.")
        except ImportError:
            self.skipTest("day187.py not found.")

    def test_day188_html_forms(self):
        """Test Day 188: HTML Form Methods"""
        # Read the raw HTML file to verify the form method is set correctly
        html_path = os.path.join(self.week3_path, 'templates', 'day188.html')
        if not os.path.exists(html_path):
            self.skipTest("day188.html not found in the templates folder.")
            
        with open(html_path, 'r') as f:
            content = f.read().upper()
            self.assertIn('METHOD="POST"', content, "Day 188 Failed: Did you set the form method to POST?")

    def test_day189_request_object(self):
        """Test Day 189: The Request Object"""
        try:
            from day189 import app
            client = app.test_client()
            # We must capture stdout to see if they printed the request method
            import io
            from contextlib import redirect_stdout
            f = io.StringIO()
            with redirect_stdout(f):
                client.get('/')
            self.assertIn("GET", f.getvalue(), "Day 189 Failed: Your script did not print the request.method to the terminal.")
        except ImportError:
            self.skipTest("day189.py not found.")

    def test_day190_form_extraction(self):
        """Test Day 190: Extracting Form Data"""
        try:
            from day190 import app
            client = app.test_client()
            # Simulate submitting the form with dummy data
            response = client.post('/login', data={'email': 'test@python.org'})
            self.assertIn(b"test@python.org", response.data, "Day 190 Failed: The script did not successfully extract the email from the form data.")
        except ImportError:
            self.skipTest("day190.py not found.")

    def test_day191_redirects(self):
        """Test Day 191: Redirecting Users"""
        try:
            from day191 import app
            client = app.test_client()
            response = client.post('/process')
            # 302 is the standard HTTP status code for a Redirect
            self.assertEqual(response.status_code, 302, "Day 191 Failed: Your route did not return a redirect response.")
        except ImportError:
            self.skipTest("day191.py not found.")

    def test_day193_capstone_contact_form(self):
        """Test Day 193: The Contact Form Capstone"""
        try:
            from day193 import app
            client = app.test_client()
            # Submit the form and tell the test client to follow the resulting redirect
            response = client.post('/contact', data={'name': 'Guido', 'message': 'Hello!'}, follow_redirects=True)
            
            self.assertEqual(response.status_code, 200, "Day 193 Failed: The contact form crashed upon submission.")
            self.assertIn(b"Message Sent", response.data, "Day 193 Failed: The success message was not flashed to the redirected page.")
            
        except ImportError:
            self.skipTest("day193.py not found.")

if __name__ == '__main__':
    unittest.main()