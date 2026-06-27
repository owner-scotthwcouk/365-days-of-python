import unittest
import subprocess
import os

class TestMonth2Week2(unittest.TestCase):

    def run_student_script(self, filename):
        """Helper function to run a student's script and capture the printed output."""
        # Navigate to the Week 2 folder where the student saves their files
        filepath = os.path.join("..", "Week_2", filename)
        
        if not os.path.exists(filepath):
            self.skipTest(f"File {filename} not found. Did you name it correctly?")
            
        # Run the script using the command line and capture what it prints
        result = subprocess.run(['python', filepath], capture_output=True, text=True)
        return result.stdout.strip() # Remove any extra hidden newline characters

    def test_day39_list_methods(self):
        """Test Day 39: Append and Insert"""
        output = self.run_student_script("day39.py")
        expected = "['orange', 'apple', 'banana', 'cherry']"
        self.assertEqual(output, expected, "Day 39 Failed: The printed list was incorrect.")

    def test_day40_sorting(self):
        """Test Day 40: Sorting and Reversing"""
        output = self.run_student_script("day40.py")
        expected = "[1-4]"
        self.assertEqual(output, expected, "Day 40 Failed: Did you sort in descending order?")

    def test_day41_list_comprehension(self):
        """Test Day 41: Even Numbers Comprehension"""
        # Assuming the challenge asks them to print a list of even numbers from 1 to 10
        output = self.run_student_script("day41.py")
        expected = "[1, 5-8]"
        self.assertEqual(output, expected, "Day 41 Failed: Only even numbers should be printed.")

    def test_day42_nested_lists(self):
        """Test Day 42: Accessing Matrix Elements"""
        # Assuming the challenge is to print the number 6 from a nested matrix
        output = self.run_student_script("day42.py")
        self.assertEqual(output, "6", "Day 42 Failed: Did not retrieve the correct nested element.")

    def test_day43_slicing(self):
        """Test Day 43: List Slicing"""
        # Assuming they need to slice and print ['c', 'd', 'e'] from a list of alphabet letters
        output = self.run_student_script("day43.py")
        expected = "['c', 'd', 'e']"
        self.assertEqual(output, expected, "Day 43 Failed: Slicing syntax is incorrect.")

    def test_day44_stacks(self):
        """Test Day 44: Stacks and pop()"""
        # Assuming they must append "Task 3" and then print the popped item
        output = self.run_student_script("day44.py")
        self.assertEqual(output, "Task 3", "Day 44 Failed: Did not pop the last item correctly.")

    def test_day45_capstone_lists(self):
        """Test Day 45: Combine, Sort, Max"""
        # Assuming they combine two lists and print the highest value (e.g., 30)
        output = self.run_student_script("day45.py")
        self.assertEqual(output, "30", "Day 45 Failed: Did not correctly combine and find the highest value.")

if __name__ == '__main__':
    unittest.main()