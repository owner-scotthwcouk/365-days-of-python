import unittest
import subprocess
import os
import sqlite3

class TestMonth6Week3(unittest.TestCase):

    def run_student_script(self, filename):
        """Helper function to run a student's script and capture the output."""
        filepath = os.path.join("..", "Week_3", filename)
        
        if not os.path.exists(filepath):
            self.skipTest(f"File {filename} not found. Did you save it in the right place?")
            
        result = subprocess.run(['python', filepath], capture_output=True, text=True)
        return result.stdout.strip()

    def test_day159_foreign_keys(self):
        """Test Day 159: Relational Keys"""
        output = self.run_student_script("day159.py")
        self.assertIn("Relational tables created!", output, "Day 159 Failed: Did you use the 'FOREIGN' keyword to define the key constraint?")

    def test_day160_inner_joins(self):
        """Test Day 160: SQL Joins"""
        output = self.run_student_script("day160.py")
        self.assertIn("INNER JOIN", open(os.path.join("..", "Week_3", "day160.py")).read().upper(), "Day 160 Failed: You must use an INNER JOIN in your SQL statement.")
        self.assertTrue(len(output) > 0, "Day 160 Failed: Your joined query did not return any results.")

    def test_day161_groupby_aggregation(self):
        """Test Day 161: COUNT and GROUP BY"""
        output = self.run_student_script("day161.py")
        self.assertIn("wrote", output, "Day 161 Failed: Did you use COUNT(title) and GROUP BY author_id?")

    def test_day162_integrity_error(self):
        """Test Day 162: Catching Database Errors"""
        output = self.run_student_script("day162.py")
        self.assertEqual(output, "Caught a duplicate entry error!", "Day 162 Failed: You did not successfully catch the sqlite3.IntegrityError.")

    def test_day163_context_managers(self):
        """Test Day 163: The 'with' keyword for DBs"""
        output = self.run_student_script("day163.py")
        
        # Verify the database was actually created and committed
        db_path = os.path.join("..", "Week_3", "data.db")
        self.assertTrue(os.path.exists(db_path), "Day 163 Failed: The data.db file was never created.")
        
        if os.path.exists(db_path):
            conn = sqlite3.connect(db_path)
            res = conn.execute("SELECT * FROM test").fetchone()
            conn.close()
            os.remove(db_path) # Clean up
            self.assertIsNotNone(res, "Day 163 Failed: The transaction was not committed using the context manager.")

    def test_day164_scraping_prep(self):
        """Test Day 164: Formatting Scraped Data"""
        output = self.run_student_script("day164.py")
        self.assertIn("('Title 1',)", output, "Day 164 Failed: Your list comprehension did not format the tags into a list of tuples.")

    def test_day165_capstone_pipeline(self):
        """Test Day 165: The Web-to-DB Pipeline Capstone"""
        output = self.run_student_script("day165.py")
        self.assertIn("Successfully inserted 2", output, "Day 165 Failed: Your executemany() function did not insert the correct number of scraped headlines.")

if __name__ == '__main__':
    unittest.main()