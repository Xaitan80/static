import unittest
from main import extract_title  # adjust import path accordingly

class TestMain(unittest.TestCase):

    def test_simple_title(self):
        md = "# Hello"
        self.assertEqual(extract_title(md), "Hello")

    def test_title_among_lines(self):
        md = """
Some intro text

# Welcome to the site

More text here
"""
        self.assertEqual(extract_title(md), "Welcome to the site")

    def test_no_title_raises(self):
        md = """
This markdown has no title
Just text and stuff
"""
        with self.assertRaises(Exception) as context:
            extract_title(md)
        self.assertIn("No level-one header found", str(context.exception))

if __name__ == "__main__":
    unittest.main()
