import unittest
import subprocess
import os

class TestMonth6Week4(unittest.TestCase):

    def run_student_script(self, filename):
        """Helper function to run a student's script and capture the output."""
        filepath = os.path.join("..", "Week_4", filename)
        
        if not os.path.exists(filepath):
            self.skipTest(f"File {filename} not found. Did you save it in the right place?")
            
        # We need to ensure the student installed sqlalchemy. 
        # If the script fails due to a ModuleNotFoundError, this will catch it.
        result = subprocess.run(['python', filepath], capture_output=True, text=True)
        if "ModuleNotFoundError" in result.stderr:
            self.fail(f"SQLAlchemy is not installed in the environment! {result.stderr}")
            
        return result.stdout.strip()

    def test_day166_create_engine(self):
        """Test Day 166: SQLAlchemy Engine"""
        output = self.run_student_script("day166.py")
        self.assertIn("Engine created: Engine(sqlite:///:memory:)", output, "Day 166 Failed: Did you use create_engine() to initialize the SQLite memory database?")

    def test_day167_declarative_base(self):
        """Test Day 167: ORM Models"""
        output = self.run_student_script("day167.py")
        self.assertIn("Mapped Table Name: users", output, "Day 167 Failed: Did you inherit from Base and set the __tablename__?")

    def test_day168_create_all(self):
        """Test Day 168: Table Generation"""
        output = self.run_student_script("day168.py")
        self.assertIn("Tables successfully generated!", output, "Day 168 Failed: Call Base.metadata.create_all(engine) to generate the tables.")

    def test_day169_orm_session(self):
        """Test Day 169: Session Commits"""
        output = self.run_student_script("day169.py")
        self.assertEqual(output, "User Alice committed to the DB!", "Day 169 Failed: Make sure you use session.add() and session.commit().")

    def test_day170_querying(self):
        """Test Day 170: Session Querying"""
        output = self.run_student_script("day170.py")
        self.assertIn("Alice's database ID is: 1", output, "Day 170 Failed: Your session.query() filter did not return the correct object ID.")

    def test_day171_updates_deletes(self):
        """Test Day 171: Modifying Objects"""
        output = self.run_student_script("day171.py")
        self.assertEqual(output, "Record updated and then deleted.", "Day 171 Failed: You did not successfully update the object and call session.delete().")

    def test_day172_capstone_orm(self):
        """Test Day 172: The ORM Capstone"""
        output = self.run_student_script("day172.py")
        self.assertTrue("Fluent Python" in output and "Clean Code" in output, "Day 172 Failed: Your for loop did not correctly query and print the book titles from the database.")

if __name__ == '__main__':
    unittest.main()