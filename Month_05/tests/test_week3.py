import unittest
import subprocess
import os

class TestMonth5Week3(unittest.TestCase):
    def run_student_script(self, filename):
        filepath = os.path.join("..", "Week_3", filename)
        if not os.path.exists(filepath):
            self.skipTest(f"File {filename} not found.")
        result = subprocess.run(['python', filepath], capture_output=True, text=True)
        return result.stdout.strip()

    def test_day131_dataframe(self):
        """Test Day 131: Creating DataFrames and Means"""
        output = self.run_student_script("day131.py")
        self.assertEqual(output, "90.0", "Day 131 Failed: Your DataFrame did not calculate the correct mean.")

    def test_day132_csv_reading(self):
        """Test Day 132: Reading a CSV with Pandas"""
        # Assuming the challenge asks them to load 'data.csv' and print the shape of the dataset
        output = self.run_student_script("day132.py")
        self.assertIn("(", output, "Day 132 Failed: Make sure you print the df.shape attribute!")

    def test_day137_capstone_data_cleaning(self):
        """Test Day 137: The Data Janitor Capstone"""
        # Assuming the capstone asks them to drop missing values and group by a category
        output = self.run_student_script("day137.py")
        self.assertIn("Cleaned Data", output, "Day 137 Failed: Your data cleaning pipeline did not output the correct results.")

if __name__ == '__main__':
    unittest.main()