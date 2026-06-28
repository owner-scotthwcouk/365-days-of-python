import unittest
import subprocess
import os
import sqlite3
from pathlib import Path

class TestMonth6Week2(unittest.TestCase):

    def run_student_script(self, filename):
        """Helper function to run a student's script and capture the output."""
        filepath = os.path.join("..", "Week_2", filename)
        
        if not os.path.exists(filepath):
            self.skipTest(f"File {filename} not found. Did you save it in the right place?")
            
        result = subprocess.run(['python', filepath], capture_output=True, text=True)
        return result.stdout.strip()

    def get_db_connection(self):
        """Helper to connect to the student's database."""
        db_path = os.path.join("..", "Week_2", "my_database.db")
        if not os.path.exists(db_path):
            self.fail("Database 'my_database.db' was not created.")
        return sqlite3.connect(db_path)

    def test_day152_create_table(self):
        """Test Day 152: Creating the Database and Table"""
        self.run_student_script("day152.py")
        
        # Connect to the DB to verify the table exists
        conn = self.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
        table_exists = cursor.fetchone()
        conn.close()
        
        self.assertIsNotNone(table_exists, "Day 152 Failed: The 'users' table was not created in the database.")

    def test_day153_insert_data(self):
        """Test Day 153: Inserting a Record"""
        self.run_student_script("day153.py")
        
        conn = self.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM users WHERE name='Guido'")
        record = cursor.fetchone()
        conn.close()
        
        self.assertIsNotNone(record, "Day 153 Failed: The name 'Guido' was not inserted or committed to the database.")

    def test_day154_query_data(self):
        """Test Day 154: SELECT Queries"""
        output = self.run_student_script("day154.py")
        self.assertIn("Guido", output, "Day 154 Failed: Did you fetchall() and print the results?")

    def test_day155_where_clause(self):
        """Test Day 155: Parameterized WHERE Queries"""
        output = self.run_student_script("day155.py")
        self.assertIn("Guido", output, "Day 155 Failed: Your fetchone() call did not print the correct parameterized result.")

    def test_day156_update_data(self):
        """Test Day 156: The UPDATE Command"""
        self.run_student_script("day156.py")
        
        conn = self.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM users WHERE name='Guido van Rossum'")
        updated_record = cursor.fetchone()
        conn.close()
        
        self.assertIsNotNone(updated_record, "Day 156 Failed: The record was not updated to 'Guido van Rossum'.")

    def test_day157_delete_data(self):
        """Test Day 157: The DELETE Command"""
        self.run_student_script("day157.py")
        
        conn = self.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM users WHERE name='Guido van Rossum'")
        deleted_record = cursor.fetchone()
        conn.close()
        
        self.assertIsNone(deleted_record, "Day 157 Failed: The record 'Guido van Rossum' was not successfully deleted.")

    def test_day158_capstone_memory_db(self):
        """Test Day 158: RAM Database and executemany()"""
        output = self.run_student_script("day158.py")
        self.assertTrue("Python Crash Course" in output and "Fluent Python" in output, 
                        "Day 158 Failed: Your memory database did not execute or print the multiple records correctly.")

if __name__ == '__main__':
    unittest.main()