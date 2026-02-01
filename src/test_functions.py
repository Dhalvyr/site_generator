import unittest
from functions import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_simple_case(self):
        old_node = TextNode("This is a text with a **bold** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([old_node], "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is a text with a ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" word", TextType.TEXT)
            ]
        )

    def test_no_delimiter(self):
        old_node = TextNode("This is just text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([old_node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [old_node])

    def test_invalid_markdown(self):
        old_node = TextNode("This is **invalid", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([old_node], "**", TextType.BOLD)

    def test_wrong_delimiter(self):
        old_node = TextNode("This is a text with an _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([old_node], "**", TextType.BOLD)
        self.assertEqual([old_node], new_nodes)

    def test_no_text_type(self):
        old_node = TextNode("**This is all bold**", TextType.BOLD)
        new_nodes = split_nodes_delimiter([old_node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [old_node])

    def test_no_text_type_check_another_type(self):
        old_node = TextNode("**This is all bold**", TextType.BOLD)
        new_nodes = split_nodes_delimiter([old_node], "_", TextType.ITALIC)
        self.assertEqual(new_nodes, [old_node])

    def test_several_nodes(self):
        old_node = TextNode("This is a sentence", TextType.TEXT)
        old_node2 = TextNode("This one has a **bold** word", TextType.TEXT)
        old_node3 = TextNode("**This is all bold**", TextType.BOLD)
        old_nodes = [old_node, old_node2, old_node3]
        new_nodes = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is a sentence", TextType.TEXT),
                TextNode("This one has a ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
                TextNode("**This is all bold**", TextType.BOLD)
            ]
        )

if __name__ == "__main__":
    unittest.main()