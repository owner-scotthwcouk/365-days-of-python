import unittest
import subprocess
import os

class TestMonth4Week1(unittest.TestCase):
    def run_student_script(self, filename, input_data=None):
        filepath = os.path.join("..", "Week_1", filename)
        if not os.path.exists(filepath):
            self.skipTest(f"File {filename} not found.")
        result = subprocess.run(['python', filepath], input=input_data, capture_output=True, text=True)
        return result.stdout.strip()

    def test_day89_try_except(self):
        """Test Day 89: Catching a ZeroDivisionError"""
        output = self.run_student_script("day89.py")
        self.assertEqual(output, "Caught a division error!", "Day 89 Failed: Your except block did not catch the error.")

    def test_day90_multiple_exceptions(self):
        """Test Day 90: Handling different error types"""
        output = self.run_student_script("day90.py", input_data="not_a_number\n")
        self.assertIn("Invalid input", output, "Day 90 Failed: Did you catch the ValueError?")

    def test_day91_finally_block(self):
        """Test Day 91: The 'finally' keyword"""
        output = self.run_student_script("day91.py")
        self.assertTrue(output.endswith("Execution complete"), "Day 91 Failed: Ensure the finally block prints the required string.")

    def test_day95_capstone_safe_calculator(self):
        """Test Day 95: The Crash-Proof Calculator"""
        output = self.run_student_script("day95.py", input_data="ten\n")
        self.assertIn("Error: Please enter numbers only", output, "Day 95 Failed: Your calculator crashed on bad input instead of handling it.")

if __name__ == '__main__':
    unittest.main()