import unittest
import subprocess
import os

class TestMonth3Week4(unittest.TestCase):

    def run_student_script(self, filename, input_data=None):
        """Helper function to run a student's script and capture the output."""
        filepath = os.path.join("..", "Week_4", filename)
        
        if not os.path.exists(filepath):
            self.skipTest(f"File {filename} not found. Did you save it in the right place?")
            
        result = subprocess.run(
            ['python', filepath], 
            input=input_data, 
            capture_output=True, 
            text=True
        )
        return result.stdout.strip(), result.stderr.strip()

    def test_day82_try_except(self):
        """Test Day 82: Basic Error Catching"""
        stdout, stderr = self.run_student_script("day82.py")
        # Ensure the script did not actually crash (stderr should be empty)
        self.assertEqual(stderr, "", "Day 82 Failed: Your program actually crashed! Did you use try/except?")
        self.assertEqual(stdout, "You cannot divide by zero!", "Day 82 Failed: The except block did not print the correct message.")

    def test_day83_finally(self):
        """Test Day 83: The finally keyword"""
        # Assuming Day 83 asks them to use 'finally' to print "Execution complete" no matter what happens
        stdout, _ = self.run_student_script("day83.py")
        self.assertIn("Execution complete", stdout, "Day 83 Failed: The finally block did not execute.")

    def test_day84_raising_exceptions(self):
        """Test Day 84: The raise keyword"""
        stdout, _ = self.run_student_script("day84.py")
        self.assertEqual(stdout, "Age cannot be negative!", "Day 84 Failed: The custom ValueError was not raised or caught properly.")

    def test_day85_custom_exception_classes(self):
        """Test Day 85: Building Custom Exception Objects"""
        # Assuming Day 85 challenges them to inherit from Python's base Exception class to make a custom error
        stdout, _ = self.run_student_script("day85.py")
        self.assertTrue(stdout != "", "Day 85 Failed: Did your custom exception class work?")

    def test_day86_to_90_capstone(self):
        """Test Days 86-90: Month 3 Final Capstone"""
        # Assuming the Month 3 Capstone is an interactive menu that relies on classes and robust error handling 
        # (e.g. typing a string when a number is expected shouldn't crash the program)
        stdout, stderr = self.run_student_script("day90.py", input_data="invalid_text\n3\n")
        self.assertEqual(stderr, "", "Day 90 Capstone Failed: Your program crashed when given bad input!")
        self.assertIn("Invalid input caught", stdout, "Day 90 Capstone Failed: You did not catch the user's bad input gracefully.")

if __name__ == '__main__':
    unittest.main()