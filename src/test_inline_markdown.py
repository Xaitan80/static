import unittest
from inline_markdown import extract_markdown_images, extract_markdown_links, split_nodes_image, text_to_textnode, markdown_to_blocks
from htmlnode import LeafNode, ParentNode
from textnode import TextNode, TextType

class TestMarkdownExtraction(unittest.TestCase):

    #test for markdown to blocks:
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
    def test_markdown_only_whitespace(self):
        md = "   \n\n   \t  \n\n  "
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])

    def test_markdown_to_blocks_single_block(self):
        md = "This is just one paragraph with no breaks."
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["This is just one paragraph with no breaks."])

    def test_markdown_to_blocks_empty(self):
        md = ""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])

    def test_markdown_to_blocks_none(self):
        md = None
        with self.assertRaises(AttributeError):
            markdown_to_blocks(md)

    def test_markdown_to_blocks_excessive_newlines(self):
        md = "Block 1\n\n\n\n\nBlock 2\n\n\n\nBlock 3"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["Block 1", "Block 2", "Block 3"])

    def test_markdown_to_blocks_whitespace_blocks(self):
        md = "  Block 1  \n\n   Block 2   \n\n\tBlock 3\t"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["Block 1", "Block 2", "Block 3"])

    #end of tests for block

      
    #test for text_to_textnode
    def test_plain_text(self):
        text = "Hello world"
        result = text_to_textnode(text)
        expected = [TextNode("Hello world", TextType.TEXT)]
        self.assertEqual(result, expected)

    def test_bold_text(self):
        text = "Hello **bold** world"
        result = text_to_textnode(text)
        expected = [
            TextNode("Hello ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" world", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_italic_text(self):
        text = "Hello *italic* world"
        result = text_to_textnode(text)
        expected = [
            TextNode("Hello ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" world", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_code_text(self):
        text = "use `code` snippets"
        result = text_to_textnode(text)
        expected = [
            TextNode("use ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" snippets", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_image_node(self):
        text = "Look at this ![alt](image.png)"
        result = text_to_textnode(text)
        expected = [
            TextNode("Look at this ", TextType.TEXT),
            TextNode("alt", TextType.IMAGE, url="image.png"),
        ]
        self.assertEqual(result, expected)

    def test_link_node(self):
        text = "Check out [test](https://test.com)"
        result = text_to_textnode(text)
        expected = [
            TextNode("Check out ", TextType.TEXT),
            TextNode("test", TextType.LINK, url="https://test.com"),
        ]
        self.assertEqual(result, expected)

    def test_combined_formatting(self):
        text = "**bold** and *italic* with `code` and ![img](x.png) + [link](y.com)"
        result = text_to_textnode(text)
        expected = [
            TextNode("bold", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" with ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" and ", TextType.TEXT),
            TextNode("img", TextType.IMAGE, url="x.png"),
            TextNode(" + ", TextType.TEXT),
            TextNode("link", TextType.LINK, url="y.com"),
        ]
        self.assertEqual(result, expected)


    #end of test for text_to_textnode
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
