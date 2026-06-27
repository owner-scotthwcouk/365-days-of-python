import unittest
import subprocess
import os

class TestMonth1Week2(unittest.TestCase):

    def run_student_script(self, filename, input_data=None):
        """
        Helper function to run a student's script. 
        The 'input_data' argument allows us to simulate a user typing into the terminal!
        """
        filepath = os.path.join("..", "Week_2", filename)
        
        if not os.path.exists(filepath):
            self.skipTest(f"File {filename} not found. Did you save it in the right place?")
            
        # Run the script, inject the simulated input, and capture the output
        result = subprocess.run(
            ['python', filepath], 
            input=input_data,       # This types our test data into the user's input() prompt
            capture_output=True, 
            text=True
        )
        return result.stdout.strip()

    def test_day06_user_input(self):
        """Test Day 6: User Input"""
        # We simulate the user typing "Guido" and hitting Enter (\n)
        output = self.run_student_script("day06.py", input_data="Guido\n")
        
        # The output will include the prompt text PLUS the greeting
        self.assertIn("Hello, Guido!", output, "Day 6 Failed: The greeting did not format the input correctly.")

    def test_day07_if_else(self):
        """Test Day 7: If / Else Logic"""
        output = self.run_student_script("day07.py")
        expected = "You can vote!"
        self.assertEqual(output, expected, "Day 7 Failed: The wrong condition was printed.")

    def test_day08_elif(self):
        """Test Day 8: Multiple Conditions"""
        # Assuming Day 8 asks them to print "Zero", "Positive", or "Negative" based on a variable
        output = self.run_student_script("day08.py")
        self.assertIn(output, ["Zero", "Positive", "Negative"], "Day 8 Failed: Did you use an elif statement?")

    def test_day09_while_loops(self):
        """Test Day 9: The While Loop"""
        # Assuming Day 9 asks them to print numbers 1 through 3
        output = self.run_student_script("day09.py")
        self.assertIn("1\n2\n3", output, "Day 9 Failed: The while loop did not output the correct sequence.")

    def test_day10_capstone_login(self):
        """Test Day 10: The Login Gate"""
        # Assuming the Capstone combines input() and if/else to check a password
        success_output = self.run_student_script("day10.py", input_data="secret_password\n")
        self.assertIn("Access Granted", success_output, "Day 10 Failed: Did not grant access for the correct password.")
        
        fail_output = self.run_student_script("day10.py", input_data="wrong_password\n")
        self.assertIn("Access Denied", fail_output, "Day 10 Failed: Did not deny access for an incorrect password.")

if __name__ == '__main__':
    unittest.main()
