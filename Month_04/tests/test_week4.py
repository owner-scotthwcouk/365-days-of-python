import unittest
import subprocess
import os

class TestMonth4Week4(unittest.TestCase):
    def run_student_script(self, filename):
        filepath = os.path.join("..", "Week_4", filename)
        if not os.path.exists(filepath):
            self.skipTest(f"File {filename} not found.")
        result = subprocess.run(['python', filepath], capture_output=True, text=True)
        return result.stdout.strip()

    def test_day110_random(self):
        """Test Day 110: The random module"""
        output = self.run_student_script("day110.py")
        self.assertIn("Your lucky number is", output, "Day 110 Failed: Did you import random and print the output string?")

    def test_day111_datetime(self):
        """Test Day 111: The datetime module"""
        # Assuming the challenge asks them to print the current year using datetime.now().year
        output = self.run_student_script("day111.py")
        self.assertTrue(output.isdigit(), "Day 111 Failed: You should only be printing the current numerical year.")

    def test_day112_collections(self):
        """Test Day 112: Counter from collections"""
        output = self.run_student_script("day112.py")
        self.assertIn("Counter", output, "Day 112 Failed: Did you use the collections.Counter class to count the list items?")

    def test_day116_capstone_stdlib(self):
        """Test Day 116: Standard Library Capstone"""
        output = self.run_student_script("day116.py")
        self.assertIn("Simulation complete", output, "Day 116 Failed: Your master simulation using itertools, math, and random did not finish.")

if __name__ == '__main__':
    unittest.main()