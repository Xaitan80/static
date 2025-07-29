import unittest
from htmlnode import LeafNode, ParentNode
from textnode import TextNode, TextType
from delimiters import split_nodes_delimiter  # adjust import path if needed


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_basic_split(self):
        input_nodes = [TextNode("This is *bold* text", TextType.TEXT)]
        output = split_nodes_delimiter(input_nodes, "*", TextType.BOLD)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT),
        ]
        self.assertEqual(output, expected)

    def test_multiple_splits(self):
        input_nodes = [TextNode("This is *bold* and *important*", TextType.TEXT)]
        output = split_nodes_delimiter(input_nodes, "*", TextType.BOLD)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("important", TextType.BOLD),
            TextNode("", TextType.TEXT),
        ]
        self.assertEqual(output, expected)

    def test_no_delimiter(self):
        input_nodes = [TextNode("Nothing special here", TextType.TEXT)]
        output = split_nodes_delimiter(input_nodes, "*", TextType.BOLD)
        expected = [TextNode("Nothing special here", TextType.TEXT)]
        self.assertEqual(output, expected)

    def test_odd_delimiters(self):
        input_nodes = [TextNode("This is *not* closed properly*", TextType.TEXT)]
        output = split_nodes_delimiter(input_nodes, "*", TextType.BOLD)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("not", TextType.BOLD),
            TextNode(" closed properly", TextType.TEXT),
            TextNode("", TextType.BOLD),
        ]
        self.assertEqual(output, expected)

    def test_non_text_node_untouched(self):
        input_nodes = [TextNode("Normal", TextType.BOLD)]
        output = split_nodes_delimiter(input_nodes, "*", TextType.ITALIC)
        expected = [TextNode("Normal", TextType.BOLD)]
        self.assertEqual(output, expected)


if __name__ == "__main__":
    unittest.main()
