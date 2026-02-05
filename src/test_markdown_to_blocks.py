import unittest
from markdown_to_blocks import (
    markdown_to_blocks,
    block_to_block_type,
    BlockType,
)

class TextMarkdownToBlocks(unittest.TestCase):
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

class TestBlockToBlockTypes(unittest.TestCase):
        def test_heading(self):
            block = "# heading"
            self.assertEqual(block_to_block_type(block), BlockType.HEADING)

        def test_cod(self):
            block = "```\ncode\n```"
            self.assertEqual(block_to_block_type(block), BlockType.CODE)

        def test_quote(self):
            block = ">quote"
            self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

        def test_unordered_list(self):
            block = "- an element\n- another element\n- other element"
            self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

        def test_ordered_list(self):
            block = "1. first element\n2. second element\n3. third element"
            self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

        def test_paragraph(self):
            block = "this is a paragraph"
            self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
             

     

if __name__ == "__main__":
    unittest.main()