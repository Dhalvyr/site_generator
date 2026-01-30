import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_empty_dict(self):
        node = HTMLNode(props={})
        self.assertEqual("", node.props_to_html())

    def test_dict_is_none(self):
        node = HTMLNode(props=None)
        self.assertEqual("", node.props_to_html())
    
    def test_one_element_dict(self):
        dictionary = {"href": "https://www.google.com"}
        node = HTMLNode(props=dictionary)
        self.assertEqual(
            ' href="https://www.google.com"',
            node.props_to_html()
        )

    def test_several_element_dict(self):
        dictionary = {"href": "https://www.google.com", "target": "_blank"}
        node = HTMLNode(props=dictionary)
        self.assertEqual(
            ' href="https://www.google.com" target="_blank"',
            node.props_to_html()
        )
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_repr(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(
            node.__repr__(),
            'LeafNode(p, Hello, world!, None)'
            )
    
    def test_leaf_no_value(self):
        node = LeafNode("p", value=None)
        self.assertRaises(ValueError, node.to_html)
    
    def test_leaf_no_tag(self):
        node = LeafNode(tag= None, value="Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")
