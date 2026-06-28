import unittest
import subprocess
import os

class TestMonth3Week1(unittest.TestCase):

    def run_student_script(self, filename):
        """Helper function to run a student's script and capture the output."""
        filepath = os.path.join("..", "Week_1", filename)
        
        if not os.path.exists(filepath):
            self.skipTest(f"File {filename} not found. Did you save it in the right place?")
            
        result = subprocess.run(['python', filepath], capture_output=True, text=True)
        return result.stdout.strip()

    def test_day61_classes(self):
        """Test Day 61: Creating a Class"""
        output = self.run_student_script("day61.py")
        self.assertIn("__main__.Dog", output, "Day 61 Failed: Did you create the Dog class and print its type?")

    def test_day62_init_method(self):
        """Test Day 62: Instance Attributes"""
        output = self.run_student_script("day62.py")
        self.assertEqual(output, "Fido", "Day 62 Failed: The object's name attribute was not assigned or printed correctly.")

    def test_day63_custom_methods(self):
        """Test Day 63: Adding Methods"""
        # Assuming Day 63 asks them to add a bark() method that prints "Woof!"
        output = self.run_student_script("day63.py")
        self.assertEqual(output, "Woof!", "Day 63 Failed: The bark() method did not print the correct string.")

    def test_day64_multiple_objects(self):
        """Test Day 64: Independent Instances"""
        # Assuming Day 64 asks them to create two dogs, "Rex" and "Buddy", and print their names
        output = self.run_student_script("day64.py")
        self.assertTrue("Rex" in output and "Buddy" in output, "Day 64 Failed: Did you instantiate and print both objects?")

    def test_day65_modifying_attributes(self):
        """Test Day 65: Updating Object State"""
        # Assuming Day 65 asks them to change a Dog's age from 3 to 4 and print it
        output = self.run_student_script("day65.py")
        self.assertEqual(output, "4", "Day 65 Failed: You did not successfully update and print the new age attribute.")

    def test_day66_default_attributes(self):
        """Test Day 66: Default Values in __init__"""
        # Assuming Day 66 asks them to set a default 'is_hungry' attribute to True
        output = self.run_student_script("day66.py")
        self.assertEqual(output, "True", "Day 66 Failed: The default attribute was not set correctly.")

    def test_day67_capstone_bank_account(self):
        """Test Day 67: OOP Capstone"""
        # Assuming the Capstone challenges them to build a BankAccount class with deposit() and withdraw() methods
        # The script should perform some math and print the final balance (e.g., 150)
        output = self.run_student_script("day67.py")
        self.assertEqual(output, "150", "Day 67 Failed: Your BankAccount methods did not calculate the correct final balance.")

if __name__ == '__main__':
    unittest.main()