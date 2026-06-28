import unittest
import subprocess
import os
from pathlib import Path

class TestMonth5Week2(unittest.TestCase):
    def run_student_script(self, filename):
        filepath = os.path.join("..", "Week_2", filename)
        if not os.path.exists(filepath):
            self.skipTest(f"File {filename} not found.")
        result = subprocess.run(['python', filepath], capture_output=True, text=True)
        return result.stdout.strip()

    def test_day124_pathlib(self):
        """Test Day 124: Getting Absolute Paths"""
        output = self.run_student_script("day124.py")
        self.assertTrue(len(output) > 0 and ("/" in output or "\\" in output), "Day 124 Failed: Did you use the resolve() or absolute() method?")

    def test_day125_making_directories(self):
        """Test Day 125: Creating Folders"""
        self.run_student_script("day125.py")
        target_dir = Path("..") / "Week_2" / "new_folder"
        self.assertTrue(target_dir.exists(), "Day 125 Failed: Your script did not create the required directory.")
        if target_dir.exists():
            target_dir.rmdir() # Clean up

    def test_day130_capstone_file_organizer(self):
        """Test Day 130: The Bulk File Organizer"""
        self.run_student_script("day130.py")
        # Assuming the capstone challenges them to move all .txt files into a 'TextFiles' folder
        success_check = Path("..") / "Week_2" / "TextFiles"
        self.assertTrue(success_check.exists(), "Day 130 Failed: Your script did not successfully organize the files into the target folder.")

if __name__ == '__main__':
    unittest.main()