import unittest
import subprocess
import os

class TestMonth4Week2(unittest.TestCase):
    def run_student_script(self, filename):
        filepath = os.path.join("..", "Week_2", filename)
        if not os.path.exists(filepath):
            self.skipTest(f"File {filename} not found.")
        result = subprocess.run(['python', filepath], capture_output=True, text=True)
        return result.stdout.strip()

    def test_day96_yield(self):
        """Test Day 96: Basic Generators"""
        output = self.run_student_script("day96.py")
        self.assertEqual(output, "1\n2\n3", "Day 96 Failed: The generator did not yield the correct sequence.")

    def test_day97_next_function(self):
        """Test Day 97: Manually stepping with next()"""
        output = self.run_student_script("day97.py")
        self.assertEqual(output, "Step 1", "Day 97 Failed: You should only print the first yield using next().")

    def test_day102_capstone_data_stream(self):
        """Test Day 102: Generator Capstone"""
        output = self.run_student_script("day102.py")
        self.assertIn("Memory limit safe", output, "Day 102 Failed: Your data stream capstone failed its memory check.")

if __name__ == '__main__':
    unittest.main()