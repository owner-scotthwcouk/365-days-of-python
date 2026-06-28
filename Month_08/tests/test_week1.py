import unittest
import os
import sys

class TestMonth8Week1(unittest.TestCase):
    def setUp(self):
        # Dynamically add the Week 1 folder to the system path
        self.week1_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../Week_1'))
        sys.path.insert(0, self.week1_path)

    def tearDown(self):
        if self.week1_path in sys.path:
            sys.path.remove(self.week1_path)

    def test_day201_hello_fastapi(self):
        """Test Day 201: Basic FastAPI Setup"""
        try:
            from day201 import app
            from fastapi.testclient import TestClient
            client = TestClient(app)
            response = client.get("/")
            self.assertEqual(response.status_code, 200, "Day 201 Failed: Endpoint did not return a 200 status code.")
            self.assertEqual(response.json(), {"message": "Hello, FastAPI!"}, "Day 201 Failed: Incorrect JSON response.")
        except ImportError:
            self.skipTest("day201.py not found or app not defined.")

    def test_day202_path_parameters(self):
        """Test Day 202: Extracting Ints from the Path"""
        try:
            from day202 import app
            from fastapi.testclient import TestClient
            client = TestClient(app)
            # Test with a valid integer
            res1 = client.get("/items/42")
            self.assertEqual(res1.json().get("item_id"), 42, "Day 202 Failed: Did not correctly parse the integer path parameter.")
            
            # Test FastAPI's automatic validation (sending a string instead of an int should fail)
            res2 = client.get("/items/not_a_number")
            self.assertEqual(res2.status_code, 422, "Day 202 Failed: You did not enforce the item_id to be an 'int' type.")
        except ImportError:
            self.skipTest("day202.py not found.")

    def test_day203_query_parameters(self):
        """Test Day 203: Query Strings"""
        try:
            from day203 import app
            from fastapi.testclient import TestClient
            client = TestClient(app)
            response = client.get("/users/?skip=5&limit=20")
            self.assertEqual(response.json().get("limit"), 20, "Day 203 Failed: Did not return the limit query parameter.")
        except ImportError:
            self.skipTest("day203.py not found.")

    def test_day204_pydantic_models(self):
        """Test Day 204: Pydantic BaseModel"""
        try:
            from day204 import Product
            # Ensure it can be instantiated
            item = Product(name="Test", price=9.99)
            self.assertEqual(item.name, "Test", "Day 204 Failed: The Product model does not have the 'name' attribute.")
            self.assertEqual(item.price, 9.99, "Day 204 Failed: The Product model does not have the 'price' attribute.")
        except ImportError:
            self.skipTest("day204.py not found.")

    def test_day205_post_requests(self):
        """Test Day 205: POSTing Pydantic Models"""
        try:
            from day205 import app
            from fastapi.testclient import TestClient
            client = TestClient(app)
            response = client.post("/products/", json={"name": "Monitor", "price": 49.99})
            self.assertEqual(response.status_code, 200, "Day 205 Failed: The POST route crashed or was not defined.")
            self.assertEqual(response.json().get("received_name"), "Monitor", "Day 205 Failed: Did not successfully extract the name from the POST body.")
        except ImportError:
            self.skipTest("day205.py not found.")

    def test_day207_capstone_api(self):
        """Test Day 207: The Book Inventory API Capstone"""
        try:
            from day207 import app
            from fastapi.testclient import TestClient
            client = TestClient(app)
            
            # Post a new book
            post_res = client.post("/books/", json={"title": "Automate the Boring Stuff", "author": "Al Sweigart", "pages": 504})
            self.assertEqual(post_res.status_code, 200, "Day 207 Failed: The POST route is not accepting the Book model.")
            
            # Get the list of books to ensure it was added
            get_res = client.get("/books/")
            self.assertTrue(len(get_res.json()) > 0, "Day 207 Failed: The simulated database is empty after POSTing a book.")
            self.assertEqual(get_res.json().get("title"), "Automate the Boring Stuff", "Day 207 Failed: The fetched book does not match the inserted data.")
            
        except ImportError:
            self.skipTest("day207.py not found.")

if __name__ == '__main__':
    unittest.main()