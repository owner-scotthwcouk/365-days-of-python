import unittest
import subprocess
import os

class TestMonth5Week1(unittest.TestCase):
    def run_student_script(self, filename):
        filepath = os.path.join("..", "Week_1", filename)
        if not os.path.exists(filepath):
            self.skipTest(f"File {filename} not found.")
        result = subprocess.run(['python', filepath], capture_output=True, text=True)
        return result.stdout.strip()

    def test_day117_json_loads(self):
        """Test Day 117: Parsing JSON strings"""
        output = self.run_student_script("day117.py")
        self.assertEqual(output, "Guido", "Day 117 Failed: Did you use json.loads() to parse the data?")

    def test_day118_json_dumps(self):
        """Test Day 118: Converting Dicts to JSON"""
        output = self.run_student_script("day118.py")
        self.assertTrue(output.startswith("{") and '"age":' in output, "Day 118 Failed: You did not successfully serialize the dictionary to JSON.")

    def test_day123_capstone_api_fetch(self):
        """Test Day 123: The Fake API Capstone"""
        # Assuming the capstone asks them to use the 'requests' library to fetch and print a specific JSON key
        output = self.run_student_script("day123.py")
        self.assertIn("Success", output, "Day 123 Failed: Your script did not successfully extract the target key from the API response.")

if __name__ == '__main__':
    unittest.main()