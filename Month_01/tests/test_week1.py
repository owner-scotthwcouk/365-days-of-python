import unittest
import subprocess
import os

class TestMonth1Week1(unittest.TestCase):

    def run_student_script(self, filename):
        """Helper function to run a student's script and capture the printed output."""
        # Navigate to the Week 1 folder
        filepath = os.path.join("..", "Week_1", filename)
        
        if not os.path.exists(filepath):
            self.skipTest(f"File {filename} not found. Did you save it in the right place?")
            
        # Run the script and capture the terminal output
        result = subprocess.run(['python', filepath], capture_output=True, text=True)
        return result.stdout.strip() 

    def test_day01_hello_world(self):
        """Test Day 1: Hello, World!"""
        output = self.run_student_script("day01.py")
        expected = "Hello, World!"
        self.assertEqual(output, expected, "Day 1 Failed: Check your spelling and punctuation!")

    def test_day02_variables(self):
        """Test Day 2: String Formatting"""
        output = self.run_student_script("day02.py")
        expected = "I am learning Python!"
        self.assertEqual(output, expected, "Day 2 Failed: Did you inject the variable correctly?")

    def test_day03_basic_math(self):
        """Test Day 3: Calculating Area"""
        # Assuming the Day 3 challenge asks them to print the area of a 5x8 rectangle (40)
        output = self.run_student_script("day03.py")
        expected = "40"
        self.assertEqual(output, expected, "Day 3 Failed: Your mathematical calculation is incorrect.")

    def test_day04_string_methods(self):
        """Test Day 4: Uppercase Transformation"""
        # Assuming the challenge asks them to print "python" in all uppercase
        output = self.run_student_script("day04.py")
        expected = "PYTHON"
        self.assertEqual(output, expected, "Day 4 Failed: Did you use the .upper() method?")

    def test_day05_capstone_receipt(self):
        """Test Day 5: The Receipt Printer"""
        # Assuming the Week 1 Capstone asks them to print a formatted receipt total
        output = self.run_student_script("day05.py")
        expected = "Total: $150"
        self.assertEqual(output, expected, "Day 5 Failed: The receipt total did not format correctly.")

if __name__ == '__main__':
    unittest.main()
