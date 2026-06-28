import unittest
import subprocess
import os

class TestMonth6Week1(unittest.TestCase):

    def run_student_script(self, filename):
        """Helper function to run a student's script and capture the output."""
        filepath = os.path.join("..", "Week_1", filename)
        
        if not os.path.exists(filepath):
            self.skipTest(f"File {filename} not found. Did you save it in the right place?")
            
        result = subprocess.run(['python', filepath], capture_output=True, text=True)
        return result.stdout.strip()

    def test_day145_fetching_html(self):
        """Test Day 145: Requests and HTML"""
        output = self.run_student_script("day145.py")
        self.assertIn("domain in literature", output.lower(), "Day 145 Failed: Did you use requests.get() and print the response.text?")

    def test_day146_beautifulsoup_parsing(self):
        """Test Day 146: Parsing a string with BS4"""
        output = self.run_student_script("day146.py")
        self.assertEqual(output, "My Webpage", "Day 146 Failed: Did you extract the soup.title.text?")

    def test_day147_finding_all_tags(self):
        """Test Day 147: find_all() method"""
        # Assuming Day 147 asks them to find all <a> tags in a string and print how many there are
        output = self.run_student_script("day147.py")
        self.assertTrue(output.isdigit(), "Day 147 Failed: You should only print the numerical length of the found tags list.")

    def test_day148_css_selectors(self):
        """Test Day 148: Scraping by Class Name"""
        # Assuming Day 148 asks them to scrape the text of a specific div with class="price"
        output = self.run_student_script("day148.py")
        self.assertIn("$", output, "Day 148 Failed: Your script did not successfully scrape the price string from the class element.")

    def test_day149_scraping_tables(self):
        """Test Day 149: Parsing HTML Tables"""
        # Assuming Day 149 asks them to parse an HTML table into a list of row data
        output = self.run_student_script("day149.py")
        self.assertTrue("[" in output and "]" in output, "Day 149 Failed: Did you extract the table rows and print them as a list?")

    def test_day150_handling_scraping_errors(self):
        """Test Day 150: HTTPError and status codes"""
        # Assuming they must use response.raise_for_status() inside a try/except block
        output = self.run_student_script("day150.py")
        self.assertIn("Failed to retrieve", output, "Day 150 Failed: Make sure you handle the 404 error cleanly!")

    def test_day151_capstone_news_scraper(self):
        """Test Day 151: The Headline Scraper Capstone"""
        # Assuming the Capstone requires them to fetch a dummy news site and print the top 3 headlines
        output = self.run_student_script("day151.py")
        self.assertIn("Headline 1:", output, "Day 151 Failed: Your scraper did not extract and format the top headlines correctly.")

if __name__ == '__main__':
    unittest.main()