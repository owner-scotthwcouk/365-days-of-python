import unittest
import subprocess
import os

class TestMonth1Week4(unittest.TestCase):

    def run_student_script(self, filename):
        """Helper function to run a student's script and capture the output."""
        filepath = os.path.join("..", "Week_4", filename)
        
        if not os.path.exists(filepath):
            self.skipTest(f"File {filename} not found. Did you save it in the right place?")
            
        result = subprocess.run(['python', filepath], capture_output=True, text=True)
        return result.stdout.strip()

    def test_day16_functions(self):
        """Test Day 16: Defining and Calling"""
        output = self.run_student_script("day16.py")
        expected = "Hello from my first function!"
        self.assertEqual(output, expected, "Day 16 Failed: Did you define and call the function correctly?")

    def test_day17_arguments(self):
        """Test Day 17: Passing Arguments"""
        output = self.run_student_script("day17.py")
        self.assertIn("Welcome to Python, Alice!", output, "Day 17 Failed: The argument was not passed or formatted correctly.")

    def test_day18_return(self):
        """Test Day 18: The Return Keyword"""
        # Assuming Day 18 asks them to write a function that returns a multiplied number and prints it
        output = self.run_student_script("day18.py")
        self.assertIn("50", output, "Day 18 Failed: Did your function return the correct calculation?")

    def test_day19_scope(self):
        """Test Day 19: Local vs Global Scope"""
        # Assuming Day 19 requires them to use a local variable inside a function without overwriting a global one
        output = self.run_student_script("day19.py")
        self.assertIn("Local", output, "Day 19 Failed: Scope collision! Make sure your function uses its own local variable.")

    def test_day20_capstone_calculator(self):
        """Test Day 20: The Calculator Capstone"""
        # Assuming the Month 1 Capstone asks them to build an add() and subtract() function
        output = self.run_student_script("day20.py")
        self.assertTrue("10" in output and "5" in output, "Day 20 Failed: Your calculator functions did not return the right numbers.")

if __name__ == '__main__':
    unittest.main()
