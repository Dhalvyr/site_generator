import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_dif_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.PLAIN)
        self.assertNotEqual(node, node2)

    def test_dif_url(self):
        node = TextNode("This is a text node", TextType.PLAIN)
        node2 = TextNode("This is a text node", TextType.PLAIN, "www.someurl.com")
        self.assertNotEqual(node,node2)


if __name__ == "__main__":
    unittest.main()