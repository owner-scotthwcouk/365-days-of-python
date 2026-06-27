import unittest
import subprocess
import os

class TestMonth2Week3(unittest.TestCase):

    def run_student_script(self, filename):
        """Helper function to run a student's script and capture the output."""
        filepath = os.path.join("..", "Week_3", filename)
        
        if not os.path.exists(filepath):
            self.skipTest(f"File {filename} not found. Did you save it in the right place?")
            
        result = subprocess.run(['python', filepath], capture_output=True, text=True)
        return result.stdout.strip()

    def test_day46_dictionaries(self):
        """Test Day 46: Adding a Dictionary Key"""
        output = self.run_student_script("day46.py")
        self.assertIn("'city': 'New York'", output, "Day 46 Failed: Did you add the 'city' key to the dictionary?")

    def test_day47_dict_iteration(self):
        """Test Day 47: Looping through Keys and Values"""
        # Assuming Day 47 asks them to loop through the dictionary and print "key: value"
        output = self.run_student_script("day47.py")
        self.assertIn("name: Alice", output, "Day 47 Failed: The dictionary was not iterated correctly.")

    def test_day48_sets(self):
        """Test Day 48: Removing Duplicates with Sets"""
        output = self.run_student_script("day48.py")
        expected = "{1, 2, 3, 4}"
        self.assertEqual(output, expected, "Day 48 Failed: The set did not remove duplicates correctly. Check your syntax!")

    def test_day49_set_operations(self):
        """Test Day 49: Intersections and Unions"""
        # Assuming Day 49 asks them to find the intersection of two sets and print the shared value
        output = self.run_student_script("day49.py")
        self.assertTrue(output.isdigit(), "Day 49 Failed: The output should just be the shared number.")

    def test_day50_dict_methods(self):
        """Test Day 50: The .get() Method"""
        # Assuming Day 50 challenges them to use .get() to safely retrieve a missing key without crashing
        output = self.run_student_script("day50.py")
        self.assertIn("Not Found", output, "Day 50 Failed: Make sure you provide a default fallback value for .get()!")

    def test_day51_nested_data(self):
        """Test Day 51: Dictionaries inside Dictionaries"""
        # Assuming they have to print the age of a specific person inside a nested dict
        output = self.run_student_script("day51.py")
        self.assertEqual(output, "30", "Day 51 Failed: You did not access the correct nested value.")

    def test_day52_capstone(self):
        """Test Day 52: Data Structure Capstone"""
        # Assuming the capstone asks them to count the frequency of words in a list and store them in a dict
        output = self.run_student_script("day52.py")
        self.assertIn("'python': 3", output.lower(), "Day 52 Failed: The word frequency dictionary is incorrect.")

if __name__ == '__main__':
    unittest.main()