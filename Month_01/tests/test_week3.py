import unittest
import subprocess
import os

class TestMonth1Week3(unittest.TestCase):

    def run_student_script(self, filename):
        """Helper function to run a student's script and capture the output."""
        filepath = os.path.join("..", "Week_3", filename)
        
        if not os.path.exists(filepath):
            self.skipTest(f"File {filename} not found. Did you save it in the right place?")
            
        result = subprocess.run(['python', filepath], capture_output=True, text=True)
        return result.stdout.strip()

    def test_day11_lists(self):
        """Test Day 11: Creating a List"""
        output = self.run_student_script("day11.py")
        # Check if the output looks like a Python list
        self.assertTrue(output.startswith("[") and output.endswith("]"), "Day 11 Failed: The output is not a formatted list.")
        self.assertIn("apple", output.lower(), "Day 11 Failed: Make sure 'apple' is in your list!")

    def test_day12_for_loops(self):
        """Test Day 12: Basic Iteration"""
        output = self.run_student_script("day12.py")
        expected = "apple\nbanana\ncherry"
        self.assertEqual(output, expected, "Day 12 Failed: The loop did not print each fruit on a new line.")

    def test_day13_range(self):
        """Test Day 13: Using range()"""
        # Assuming Day 13 asks them to print numbers 1 through 5 using range(1, 6)
        output = self.run_student_script("day13.py")
        expected = "1\n2\n3\n4\n5"
        self.assertEqual(output, expected, "Day 13 Failed: The range() function did not output the correct numbers.")

    def test_day14_break_continue(self):
        """Test Day 14: Break and Continue"""
        # Assuming they must loop 1 to 5, but 'continue' on 3
        output = self.run_student_script("day14.py")
        expected = "1\n2\n4\n5"
        self.assertEqual(output, expected, "Day 14 Failed: Did you use the 'continue' keyword to skip the number 3?")

    def test_day15_capstone_iteration(self):
        """Test Day 15: The Loop Capstone"""
        # Assuming the Capstone requires them to loop through a list of prices and print the total sum
        output = self.run_student_script("day15.py")
        self.assertIn("150", output, "Day 15 Failed: Your loop did not calculate the correct total sum.")

if __name__ == '__main__':
    unittest.main()
