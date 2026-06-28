import unittest
import subprocess
import os

class TestMonth3Week3(unittest.TestCase):

    def run_student_script(self, filename):
        """Helper function to run a student's script and capture the output."""
        filepath = os.path.join("..", "Week_3", filename)
        
        if not os.path.exists(filepath):
            self.skipTest(f"File {filename} not found. Did you save it in the right place?")
            
        result = subprocess.run(['python', filepath], capture_output=True, text=True)
        return result.stdout.strip()

    def test_day75_str_method(self):
        """Test Day 75: The __str__ Method"""
        output = self.run_student_script("day75.py")
        expected = "Book Title: 365 Days of Python"
        self.assertEqual(output, expected, "Day 75 Failed: Your __str__ method did not format the output correctly.")

    def test_day76_math_dunders(self):
        """Test Day 76: Overloading Operators with __add__"""
        # Assuming Day 76 asks them to use __add__ to add the value of two separate objects together
        output = self.run_student_script("day76.py")
        self.assertTrue(output.isdigit(), "Day 76 Failed: Did you define __add__ to return the mathematical sum of the objects?")

    def test_day77_encapsulation(self):
        """Test Day 77: Private Attributes"""
        output = self.run_student_script("day77.py")
        self.assertEqual(output, "100", "Day 77 Failed: Make sure you use the get_balance() getter method to print the private variable.")

    def test_day78_property_decorators(self):
        """Test Day 78: The @property Decorator"""
        # Assuming Day 78 asks them to replace their getter method with a clean @property decorator
        output = self.run_student_script("day78.py")
        self.assertTrue(len(output) > 0, "Day 78 Failed: The property was not accessed or printed correctly.")

    def test_day79_class_methods(self):
        """Test Day 79: The @classmethod Decorator"""
        # Assuming Day 79 challenges them to use a class method to track how many total objects have been created
        output = self.run_student_script("day79.py")
        self.assertIn("Total objects:", output, "Day 79 Failed: Your class method did not track or return the correct state.")

    def test_day80_static_methods(self):
        """Test Day 80: The @staticmethod Decorator"""
        # Assuming they write a static helper method that calculates a simple math formula without needing 'self'
        output = self.run_student_script("day80.py")
        self.assertTrue(output != "", "Day 80 Failed: Your static method did not execute successfully.")

    def test_day81_capstone_inventory(self):
        """Test Day 81: Advanced OOP Capstone"""
        # Assuming the Capstone asks them to build an Inventory class using private lists and __len__ magic methods
        output = self.run_student_script("day81.py")
        self.assertIn("Inventory Size: 5", output, "Day 81 Failed: Your advanced Inventory class did not pass the final checks.")

if __name__ == '__main__':
    unittest.main()