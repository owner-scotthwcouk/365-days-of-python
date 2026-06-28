import unittest
import subprocess
import os

class TestMonth4Week3(unittest.TestCase):
    def run_student_script(self, filename):
        filepath = os.path.join("..", "Week_3", filename)
        if not os.path.exists(filepath):
            self.skipTest(f"File {filename} not found.")
        result = subprocess.run(['python', filepath], capture_output=True, text=True)
        return result.stdout.strip()

    def test_day103_simple_decorator(self):
        """Test Day 103: Decorator Syntax"""
        output = self.run_student_script("day103.py")
        expected = "Before the function runs.\nHello!\nAfter the function runs."
        self.assertEqual(output, expected, "Day 103 Failed: The decorator did not wrap the output correctly.")

    def test_day104_decorator_arguments(self):
        """Test Day 104: Using *args and **kwargs in wrappers"""
        output = self.run_student_script("day104.py")
        self.assertIn("Arguments passed securely", output, "Day 104 Failed: Did you pass *args and **kwargs into the inner function?")

    def test_day109_capstone_timer(self):
        """Test Day 109: The @timer Decorator Capstone"""
        output = self.run_student_script("day109.py")
        self.assertIn("Time elapsed:", output, "Day 109 Failed: Your custom @timer decorator did not print the elapsed execution time.")

if __name__ == '__main__':
    unittest.main()