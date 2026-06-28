import unittest
import os
import ast

class TestMonth8Week3(unittest.TestCase):
    def get_script_content(self, filename):
        """Helper function to load the student's script as text."""
        filepath = os.path.join("..", "Week_3", filename)
        if not os.path.exists(filepath):
            self.skipTest(f"File {filename} not found.")
        with open(filepath, "r") as file:
            return file.read()

    def test_day215_hello_tkinter(self):
        """Test Day 215: Tkinter Initialization"""
        content = self.get_script_content("day215.py")
        self.assertIn("tk.Tk()", content, "Day 215 Failed: You must initialize the root window using tk.Tk().")
        self.assertIn("mainloop()", content, "Day 215 Failed: You forgot to call the mainloop() at the end of the script!")

    def test_day216_widgets(self):
        """Test Day 216: Labels and Buttons"""
        content = self.get_script_content("day216.py")
        self.assertIn("tk.Label", content, "Day 216 Failed: Missing the Label widget.")
        self.assertIn("tk.Button", content, "Day 216 Failed: Missing the Button widget.")
        self.assertIn(".pack()", content, "Day 216 Failed: You must call .pack() to place the widgets in the window.")

    def test_day217_callbacks(self):
        """Test Day 217: Button Commands"""
        content = self.get_script_content("day217.py")
        self.assertTrue("command=" in content or "command =" in content, "Day 217 Failed: You did not bind a function using the 'command' parameter.")

    def test_day218_grid_layout(self):
        """Test Day 218: The Grid Manager"""
        content = self.get_script_content("day218.py")
        self.assertIn(".grid(", content, "Day 218 Failed: You must use the .grid() method instead of .pack().")
        self.assertIn("row=", content, "Day 218 Failed: Provide a 'row' argument to the grid.")
        self.assertIn("column=", content, "Day 218 Failed: Provide a 'column' argument to the grid.")

    def test_day219_user_input(self):
        """Test Day 219: Entry Widgets"""
        content = self.get_script_content("day219.py")
        self.assertIn("tk.Entry", content, "Day 219 Failed: Missing the tk.Entry() widget.")
        self.assertIn(".get()", content, "Day 219 Failed: You must use the .get() method to extract the user's typed text.")

    def test_day220_messagebox(self):
        """Test Day 220: Pop-up Alerts"""
        content = self.get_script_content("day220.py")
        self.assertIn("messagebox.showinfo", content, "Day 220 Failed: You must trigger the alert using messagebox.showinfo().")

    def test_day221_capstone_gui(self):
        """Test Day 221: The GUI Capstone"""
        content = self.get_script_content("day221.py")
        # Ensure all core elements are present for the capstone
        self.assertTrue(all(x in content for x in ["tk.Tk()", "tk.Entry", "tk.Button", "command", ".grid"]), 
                        "Day 221 Failed: Your capstone is missing one or more required components (Tk, Entry, Button, command, or grid layout).")

if __name__ == '__main__':
    unittest.main()