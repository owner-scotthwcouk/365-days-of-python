import unittest
import subprocess
import os

class TestMonth5Week4(unittest.TestCase):
    def run_student_script(self, filename):
        filepath = os.path.join("..", "Week_4", filename)
        if not os.path.exists(filepath):
            self.skipTest(f"File {filename} not found.")
        result = subprocess.run(['python', filepath], capture_output=True, text=True)
        return result.stdout.strip()

    def test_day138_re_search(self):
        """Test Day 138: Basic Regex Searching"""
        output = self.run_student_script("day138.py")
        self.assertEqual(output, "help@python.org", "Day 138 Failed: Did you call the .group() method on your match object?")

    def test_day139_re_findall(self):
        """Test Day 139: Finding Multiple Matches"""
        # Assuming the challenge asks them to extract all numbers from a string using r"\d+"
        output = self.run_student_script("day139.py")
        self.assertTrue("[" in output, "Day 139 Failed: re.findall() should return a list of matches.")

    def test_day140_re_sub(self):
        """Test Day 140: Replacing Text"""
        # Assuming the challenge asks them to censor phone numbers using re.sub()
        output = self.run_student_script("day140.py")
        self.assertIn("XXX", output, "Day 140 Failed: Did you replace the matched pattern with 'XXX'?")

    def test_day144_capstone_log_parser(self):
        """Test Day 144: Regex Capstone"""
        output = self.run_student_script("day144.py")
        self.assertIn("Errors found: 3", output, "Day 144 Failed: Your regex log parser did not accurately count the errors.")

if __name__ == '__main__':
    unittest.main()