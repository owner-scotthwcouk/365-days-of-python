import unittest
import os
import sys
from unittest.mock import patch

class TestMonth8Week4(unittest.TestCase):
    def get_script_content(self, filename):
        """Helper function to load the student's script as text."""
        filepath = os.path.join("..", "Week_4", filename)
        if not os.path.exists(filepath):
            self.skipTest(f"File {filename} not found.")
        with open(filepath, "r") as file:
            return file.read()

    @patch('matplotlib.pyplot.show')
    def test_day222_line_plot(self, mock_show):
        """Test Day 222: Basic Plotting"""
        try:
            import day222
            mock_show.assert_called_once()
            content = self.get_script_content("day222.py")
            self.assertIn("plt.plot(", content, "Day 222 Failed: You must use plt.plot() to create a line chart.")
        except ImportError:
            self.skipTest("day222.py not found.")

    @patch('matplotlib.pyplot.show')
    def test_day223_bar_charts(self, mock_show):
        """Test Day 223: Bar Charts and Labels"""
        content = self.get_script_content("day223.py")
        self.assertIn("plt.bar(", content, "Day 223 Failed: Missing plt.bar().")
        self.assertIn("plt.xlabel(", content, "Day 223 Failed: Missing the X-axis label.")
        self.assertIn("plt.ylabel(", content, "Day 223 Failed: Missing the Y-axis label.")

    @patch('matplotlib.pyplot.show')
    def test_day224_scatter_plots(self, mock_show):
        """Test Day 224: Scatter Plots"""
        content = self.get_script_content("day224.py")
        self.assertIn("plt.scatter(", content, "Day 224 Failed: You must use plt.scatter().")
        self.assertTrue("color='red'" in content.replace('"', "'"), "Day 224 Failed: Did you set the color parameter to red?")

    @patch('matplotlib.pyplot.show')
    def test_day225_seaborn_theme(self, mock_show):
        """Test Day 225: Seaborn Import and Theme"""
        content = self.get_script_content("day225.py")
        self.assertIn("import seaborn", content, "Day 225 Failed: You must import the seaborn library.")
        self.assertIn("sns.set_theme(", content, "Day 225 Failed: You forgot to apply the seaborn default theme.")

    @patch('matplotlib.pyplot.show')
    def test_day226_histograms(self, mock_show):
        """Test Day 226: Seaborn Histograms"""
        content = self.get_script_content("day226.py")
        self.assertIn("sns.histplot(", content, "Day 226 Failed: Use sns.histplot() to generate the histogram.")
        self.assertIn("kde=True", content.replace(" ", ""), "Day 226 Failed: You must set kde=True to show the distribution curve.")

    def test_day227_saving_files(self):
        """Test Day 227: Saving Plots"""
        try:
            import day227
            # Check if the file was actually generated
            file_path = os.path.join("..", "Week_4", "my_chart.png")
            self.assertTrue(os.path.exists(file_path), "Day 227 Failed: The my_chart.png file was not successfully saved to the disk.")
            if os.path.exists(file_path):
                os.remove(file_path) # Clean up after the test
        except ImportError:
            self.skipTest("day227.py not found.")

    def test_day228_capstone_dashboard(self):
        """Test Day 228: The Dashboard Capstone"""
        try:
            import day228
            file_path = os.path.join("..", "Week_4", "dashboard.png")
            self.assertTrue(os.path.exists(file_path), "Day 228 Failed: The capstone dashboard image was not saved.")
            
            content = self.get_script_content("day228.py")
            self.assertIn("plt.subplots(", content, "Day 228 Failed: You must use plt.subplots() to create the grid.")
            
            if os.path.exists(file_path):
                os.remove(file_path) # Clean up
        except ImportError:
            self.skipTest("day228.py not found.")

if __name__ == '__main__':
    unittest.main()