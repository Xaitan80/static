import unittest
from my_regex import extract_markdown_images, extract_markdown_links

class TestMarkdownExtraction(unittest.TestCase):
    def test_extract_single_image(self):
        text = "Here is an image ![alt](http://image.com/pic.png)"
        expected = [("alt", "http://image.com/pic.png")]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_extract_multiple_images(self):
        text = "![one](http://1.png) and ![two](http://2.jpg)"
        expected = [("one", "http://1.png"), ("two", "http://2.jpg")]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_extract_no_images(self):
        text = "No image here, just text"
        self.assertEqual(extract_markdown_images(text), [])

    def test_extract_single_link(self):
        text = "Here is a [link](http://example.com)"
        expected = [("link", "http://example.com")]
        self.assertEqual(extract_markdown_links(text), expected)

    def test_extract_multiple_links(self):
        text = "Go [here](http://a.com) and [there](http://b.com)"
        expected = [("here", "http://a.com"), ("there", "http://b.com")]
        self.assertEqual(extract_markdown_links(text), expected)

    def test_extract_no_links(self):
        text = "Nothing to click on here"
        self.assertEqual(extract_markdown_links(text), [])

    def test_ignores_images_in_link_function(self):
        text = "This is an image: ![alt](http://image.com)"
        self.assertEqual(extract_markdown_links(text), [])

    def test_ignores_links_in_image_function(self):
        text = "This is a link: [click](http://link.com)"
        self.assertEqual(extract_markdown_images(text), [])

if __name__ == '__main__':
    unittest.main()
