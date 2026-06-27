import unittest
import subprocess
import os

class TestMonth2Week1(unittest.TestCase):

    def run_student_script(self, filename):
        """Helper function to run a student's script and capture the output."""
        filepath = os.path.join("..", "Week_1", filename)
        
        if not os.path.exists(filepath):
            self.skipTest(f"File {filename} not found. Did you save it in the right place?")
            
        result = subprocess.run(['python', filepath], capture_output=True, text=True)
        return result.stdout.strip()

    def setUp(self):
        """Automatically create a dummy file for the Day 32 reading challenge."""
        self.data_path = os.path.join("..", "Week_1", "data.txt")
        with open(self.data_path, "w") as f:
            f.write("Secret Data")

    def tearDown(self):
        """Clean up the dummy files after the tests run."""
        if os.path.exists(self.data_path):
            os.remove(self.data_path)

    def test_day32_reading(self):
        """Test Day 32: Reading a File"""
        output = self.run_student_script("day32.py")
        self.assertEqual(output, "Secret Data", "Day 32 Failed: Your script did not read or print the file correctly.")

    def test_day33_writing(self):
        """Test Day 33: Writing to a File"""
        # Run the script so it generates the output file
        self.run_student_script("day33.py")
        
        # Check if the student's script successfully created 'output.txt'
        output_path = os.path.join("..", "Week_1", "output.txt")
        self.assertTrue(os.path.exists(output_path), "Day 33 Failed: 'output.txt' was not created.")
        
        # Verify the contents of the file
        with open(output_path, "r") as f:
            content = f.read()
            
        self.assertEqual(content, "Python is awesome!", "Day 33 Failed: The file does not contain the correct string.")
        
        # Clean up the generated file
        os.remove(output_path)

    def test_day34_appending(self):
        """Test Day 34: Appending to a File"""
        # Assuming Day 34 asks them to use "a" mode to add a line to an existing file
        output = self.run_student_script("day34.py")
        self.assertIn("Log appended", output, "Day 34 Failed: Did you use the 'a' mode to append the data?")

    def test_day35_capstone_file_parser(self):
        """Test Day 35: The File Parser Capstone"""
        # Assuming the Week 1 Capstone asks them to read a file, count the words, and write the count to a new file
        self.run_student_script("day35.py")
        result_path = os.path.join("..", "Week_1", "word_count.txt")
        self.assertTrue(os.path.exists(result_path), "Day 35 Failed: Capstone did not produce the required output file.")

if __name__ == '__main__':
    unittest.main()