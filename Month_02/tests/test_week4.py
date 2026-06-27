import unittest
import subprocess
import os

class TestMonth2Week4(unittest.TestCase):

    def run_student_script(self, filename):
        """Helper function to run a student's script and capture the output."""
        filepath = os.path.join("..", "Week_4", filename)
        
        if not os.path.exists(filepath):
            self.skipTest(f"File {filename} not found. Did you save it in the right place?")
            
        result = subprocess.run(['python', filepath], capture_output=True, text=True)
        return result.stdout.strip()

    def test_day53_tuples(self):
        """Test Day 53: Creating a Tuple"""
        output = self.run_student_script("day53.py")
        expected = "('apple', 'banana', 'cherry')"
        self.assertEqual(output, expected, "Day 53 Failed: The printed tuple was incorrect. Did you use parentheses?")

    def test_day54_unpacking(self):
        """Test Day 54: Unpacking Variables"""
        output = self.run_student_script("day54.py")
        expected = "X: 10, Y: 20"
        self.assertEqual(output, expected, "Day 54 Failed: The variables were not unpacked or printed correctly.")

    def test_day55_tuple_methods(self):
        """Test Day 55: count() and index()"""
        # Assuming Day 55 asks them to find the index of a specific item in a tuple
        output = self.run_student_script("day55.py")
        self.assertTrue(output.isdigit(), "Day 55 Failed: You should only be printing the numerical index!")

    def test_day56_lists_vs_tuples(self):
        """Test Day 56: Converting between types"""
        # Assuming Day 56 asks them to convert a list to a tuple using tuple()
        output = self.run_student_script("day56.py")
        self.assertTrue(output.startswith("(") and output.endswith(")"), "Day 56 Failed: The final output must be converted into a tuple.")

    def test_day57_zipping(self):
        """Test Day 57: The zip() function"""
        # Assuming Day 57 asks them to zip two lists together into a list of tuples
        output = self.run_student_script("day57.py")
        self.assertIn("[(", output, "Day 57 Failed: Did you use the zip() function to combine the data?")

    def test_day58_capstone_data(self):
        """Test Day 58: Month 2 Final Capstone"""
        # Assuming the Month 2 Capstone combines Lists, Dicts, Sets, and Tuples into one master script
        output = self.run_student_script("day58.py")
        self.assertIn("Data Processing Complete", output, "Day 58 Failed: Your data pipeline did not complete successfully.")

if __name__ == '__main__':
    unittest.main()