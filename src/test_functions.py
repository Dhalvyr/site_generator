import unittest
from functions import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link
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

class TestExtractLinks(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev)"
        )
        self.assertEqual([("to boot dev", "https://www.boot.dev")], matches)

class TestSplitImagesAndLinks(unittest.TestCase):
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

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](www.someurl.com) and another [second link](www.anotherurl.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "www.someurl.com"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second link", TextType.LINK, "www.anotherurl.com"
                ),
            ],
            new_nodes,
        )
    
    def test_split_image_tail_text(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and some tail text.",
            TextType.TEXT
            )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and some tail text.", TextType.TEXT)
            ],
            new_nodes
        )


    def test_split_link_tail_text(self):
        node = TextNode(
            "This is text with a [link](www.someurl.com) and some tail text.",
            TextType.TEXT
            )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "www.someurl.com"),
                TextNode(" and some tail text.", TextType.TEXT)
            ],
            new_nodes
        )

if __name__ == "__main__":
    unittest.main()