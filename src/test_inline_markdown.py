import unittest
from inline_markdown import extract_markdown_images, extract_markdown_links, split_nodes_image
from htmlnode import LeafNode, ParentNode
from textnode import TextNode, TextType

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


    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
        [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode(
                "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
            ),
        ],
        new_nodes,
    )
    def test_split_one_image(self):
        node = TextNode(
            "This is a text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,

        )
        new_node = split_nodes_image([node])
        self.assertListEqual(
        [
            TextNode("This is a text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png")
        ],
        new_node
    )
if __name__ == '__main__':
    unittest.main()
