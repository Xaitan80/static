import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_equal_different_url(self):
        node1 = TextNode("Sample text", TextType.LINK, "http://example.com")
        node2 = TextNode("Sample text", TextType.LINK, "http://different.com")
        self.assertNotEqual(node1, node2)  # Should pass

    def test_eq_same_properties(self):
        node1 = TextNode("Sample text", TextType.LINK, "http://example.com")
        node2 = TextNode("Sample text", TextType.LINK, "http://example.com")
        self.assertEqual(node1, node2)  # Should pass


    def test_not_equal_different_text_type(self):
        node1 = TextNode("Sample text", TextType.BOLD)
        node2 = TextNode("Sample text", TextType.ITALIC)
        self.assertNotEqual(node1, node2)  # Should pass

        
if __name__ == "__main__":
    unittest.main()