import unittest
import subprocess
import os

class TestMonth3Week2(unittest.TestCase):

    def run_student_script(self, filename):
        """Helper function to run a student's script and capture the output."""
        filepath = os.path.join("..", "Week_2", filename)
        
        if not os.path.exists(filepath):
            self.skipTest(f"File {filename} not found. Did you save it in the right place?")
            
        result = subprocess.run(['python', filepath], capture_output=True, text=True)
        return result.stdout.strip()

    def test_day68_inheritance(self):
        """Test Day 68: Basic Inheritance"""
        output = self.run_student_script("day68.py")
        self.assertEqual(output, "True", "Day 68 Failed: Did you pass 'Animal' into the Dog class parentheses and print the inherited attribute?")

    def test_day69_method_overriding(self):
        """Test Day 69: Overriding Methods"""
        # Assuming Day 69 asks them to override a parent speak() method with a child's version
        output = self.run_student_script("day69.py")
        self.assertIn("Meow", output, "Day 69 Failed: The child class method did not successfully override the parent's method.")

    def test_day70_super_function(self):
        """Test Day 70: Using super()"""
        output = self.run_student_script("day70.py")
        expected = "Alice runs IT"
        self.assertEqual(output, expected, "Day 70 Failed: Make sure you use super().__init__() to pass the name up to the Employee class!")

    def test_day71_isinstance(self):
        """Test Day 71: Type Checking"""
        # Assuming Day 71 challenges them to use isinstance() or issubclass() and print the boolean result
        output = self.run_student_script("day71.py")
        self.assertEqual(output, "True", "Day 71 Failed: The isinstance() check should return True.")

    def test_day72_multiple_inheritance(self):
        """Test Day 72: Inheriting from Two Classes"""
        # Assuming they must create a class that inherits from both a Flyer and Swimmer class
        output = self.run_student_script("day72.py")
        self.assertTrue("Flying" in output and "Swimming" in output, "Day 72 Failed: Your object did not inherit methods from both parent classes.")

    def test_day73_polymorphism(self):
        """Test Day 73: Polymorphism in Loops"""
        # Assuming they loop through different shapes and call a generic .area() method on each
        output = self.run_student_script("day73.py")
        self.assertTrue(output != "", "Day 73 Failed: The loop did not execute the polymorphic methods.")

    def test_day74_capstone_rpg(self):
        """Test Day 74: The RPG Character Capstone"""
        # Assuming the Capstone challenges them to build a base Character class and child Warrior/Mage classes
        output = self.run_student_script("day74.py")
        self.assertIn("Magic Missile", output, "Day 74 Failed: The Mage class did not attack correctly.")
        self.assertIn("Sword Slash", output, "Day 74 Failed: The Warrior class did not attack correctly.")

if __name__ == '__main__':
    unittest.main()