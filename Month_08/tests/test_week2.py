import unittest
import os
import sys

class TestMonth8Week2(unittest.TestCase):
    def setUp(self):
        # Dynamically add the Week 2 folder to the system path
        self.week2_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../Week_2'))
        sys.path.insert(0, self.week2_path)

    def tearDown(self):
        if self.week2_path in sys.path:
            sys.path.remove(self.week2_path)

    def test_day208_status_codes(self):
        """Test Day 208: 201 Created Status"""
        try:
            from day208 import app
            from fastapi.testclient import TestClient
            client = TestClient(app)
            response = client.post("/items/?name=Test")
            self.assertEqual(response.status_code, 201, "Day 208 Failed: Endpoint did not return a 201 Created status code.")
        except ImportError:
            self.skipTest("day208.py not found.")

    def test_day209_httpexception(self):
        """Test Day 209: 404 Exceptions"""
        try:
            from day209 import app
            from fastapi.testclient import TestClient
            client = TestClient(app)
            response = client.get("/items/999") # ID that doesn't exist
            self.assertEqual(response.status_code, 404, "Day 209 Failed: Endpoint did not safely raise a 404 HTTPException.")
            self.assertIn("not found", response.json().get("detail", "").lower(), "Day 209 Failed: Exception detail missing.")
        except ImportError:
            self.skipTest("day209.py not found.")

    def test_day210_dependencies(self):
        """Test Day 210: The Depends Keyword"""
        try:
            from day210 import app
            from fastapi.testclient import TestClient
            client = TestClient(app)
            response = client.get("/")
            self.assertEqual(response.json().get("db_status"), "Database Connection Active", "Day 210 Failed: The dependency was not successfully injected.")
        except ImportError:
            self.skipTest("day210.py not found.")

    def test_day211_model_separation(self):
        """Test Day 211: Pydantic vs SQLAlchemy"""
        try:
            from day211 import UserCreate, User
            # Test Pydantic instantiation
            p_model = UserCreate(name="Alice")
            self.assertEqual(p_model.name, "Alice", "Day 211 Failed: Pydantic model incorrect.")
            # Test SQLAlchemy table name
            self.assertEqual(User.__tablename__, "users", "Day 211 Failed: SQLAlchemy model missing __tablename__.")
        except ImportError:
            self.skipTest("day211.py not found.")

    def test_day214_capstone_api_db(self):
        """Test Day 214: The Full API-to-DB Capstone"""
        try:
            from day214 import app
            from fastapi.testclient import TestClient
            client = TestClient(app)
            
            # 1. Post a new task
            post_res = client.post("/tasks/", json={"title": "Learn FastAPI"})
            self.assertEqual(post_res.status_code, 201, "Day 214 Failed: POST route is not returning 201 Created.")
            
            # 2. Get the tasks to ensure it was saved to the DB
            get_res = client.get("/tasks/")
            tasks = get_res.json()
            self.assertTrue(len(tasks) > 0, "Day 214 Failed: Database is empty after POSTing a task.")
            self.assertEqual(tasks.get("title"), "Learn FastAPI", "Day 214 Failed: Inserted task data is incorrect.")
            
        except ImportError:
            self.skipTest("day214.py not found.")

if __name__ == '__main__':
    unittest.main()