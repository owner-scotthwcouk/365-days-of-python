import unittest
import os
import sys

class TestMonth7Week4(unittest.TestCase):
    def setUp(self):
        # Dynamically add the Week 4 folder to the system path
        self.week4_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../Week_4'))
        sys.path.insert(0, self.week4_path)

    def tearDown(self):
        if self.week4_path in sys.path:
            sys.path.remove(self.week4_path)

    def test_day194_config(self):
        """Test Day 194: Configuring SQLAlchemy"""
        try:
            from day194 import app, db
            self.assertIn('sqlite:///', app.config['SQLALCHEMY_DATABASE_URI'], "Day 194 Failed: Missing SQLite URI configuration.")
        except ImportError:
            self.skipTest("day194.py not found.")

    def test_day195_model_creation(self):
        """Test Day 195: Database Models"""
        try:
            from day195 import Post, db
            self.assertTrue(hasattr(Post, 'id') and hasattr(Post, 'title'), "Day 195 Failed: The Post model is missing the required columns.")
        except ImportError:
            self.skipTest("day195.py not found.")

    def test_day196_add_data(self):
        """Test Day 196: POST insertions"""
        try:
            from day196 import app, db, Post
            app.config['TESTING'] = True
            app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
            client = app.test_client()
            
            with app.app_context():
                db.create_all()
                client.post('/add', data={'title': 'Test Post'})
                post = Post.query.first()
                self.assertIsNotNone(post, "Day 196 Failed: The POST route did not save the object to the database.")
                self.assertEqual(post.title, "Test Post", "Day 196 Failed: The saved object does not have the correct title.")
        except ImportError:
            self.skipTest("day196.py not found.")

    def test_day198_update_data(self):
        """Test Day 198: Updating Records"""
        try:
            from day198 import app, db, Post
            app.config['TESTING'] = True
            app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
            client = app.test_client()
            
            with app.app_context():
                db.create_all()
                p = Post(title="Old Title")
                db.session.add(p)
                db.session.commit()
                
                client.get(f'/update/{p.id}')
                
                updated_post = Post.query.get(p.id)
                self.assertEqual(updated_post.title, "Updated Title!", "Day 198 Failed: Your route did not update the database object.")
        except ImportError:
            self.skipTest("day198.py not found.")

    def test_day199_delete_data(self):
        """Test Day 199: Deleting Records"""
        try:
            from day199 import app, db, Post
            app.config['TESTING'] = True
            app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
            client = app.test_client()
            
            with app.app_context():
                db.create_all()
                p = Post(title="Delete Me")
                db.session.add(p)
                db.session.commit()
                
                client.get(f'/delete/{p.id}')
                
                deleted_post = Post.query.get(p.id)
                self.assertIsNone(deleted_post, "Day 199 Failed: Your route did not delete the object from the database.")
        except ImportError:
            self.skipTest("day199.py not found.")

    def test_day200_capstone_blog(self):
        """Test Day 200: The Mini-Blog Capstone"""
        try:
            from day200 import app, db
            app.config['TESTING'] = True
            app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
            client = app.test_client()
            
            with app.app_context():
                db.create_all()
                client.post('/new', data={'content': 'My first automated blog post!'})
                response = client.get('/')
                self.assertIn(b"My first automated blog post!", response.data, "Day 200 Failed: Your database did not save or render the submitted blog post.")
        except ImportError:
            self.skipTest("day200.py not found.")

if __name__ == '__main__':
    unittest.main()