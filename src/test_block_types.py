import unittest
from block_types import block_to_block_type, BlockType

class TestBlockTypes(unittest.TestCase):

#tests for good behaviur
    def test_heading(self):
        block = "# this is a heading"
        expected = BlockType.HEADING
        self.assertEqual(block_to_block_type(block), expected)

    def test_code(self):
        block = "```"
        expected = BlockType.CODE
        self.assertEqual(block_to_block_type(block), expected)
        

    def test_quote(self):
        block = "> line one\n> line two"
        expected = BlockType.QUOTE
        self.assertEqual(block_to_block_type(block), expected)

    def test_unordered_list(self):
        block = "- line one\n- line two"
        expected = BlockType.UNORDERED_LIST
        self.assertEqual(block_to_block_type(block), expected)

    def test_ordered_list(self):
        block = "1. \n2. \n3. "
        expected = BlockType.ORDERED_LIST
        self.assertEqual(block_to_block_type(block), expected)

    def test_paragraph(self):
        block = "when nothing fits, it's a paragraph"
        expected = BlockType.PARAGRAPH
        self.assertEqual(block_to_block_type(block), expected)

# tests for bad behaviur

    def test_not_heading_symbols(self):
        for block in ['" is not a heading', '€ is also not a heading']:
            expected = BlockType.PARAGRAPH
            self.assertEqual(block_to_block_type(block), expected)

    def test_mismatched_code_block_delimiters(self):
        block = "```\nprint('hello')\n'''"
        expected = BlockType.PARAGRAPH
        self.assertEqual(block_to_block_type(block), expected)

    def test_bad_quotes(self):
        block = "<"
        expected = BlockType.PARAGRAPH
        self.assertEqual(block_to_block_type(block), expected)
   
    def test_bad_unordered_list(self):
        block = "-" #no space after - should return as paragraph
        expected = BlockType.PARAGRAPH
        self.assertEqual(block_to_block_type(block), expected)

    def test_bad_ordered_list(self):
        block = "1. First item\n3. Third item"  # Skips 2, so it's invalid
        expected = BlockType.PARAGRAPH
        self.assertEqual(block_to_block_type(block), expected)





    
        






if __name__ == "__main__":
    unittest.main()

