import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

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

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_parent_no_child(self):
        parent_node = ParentNode("div", [])
        self.assertRaises(ValueError, parent_node.to_html)

    def test_parent_no_tag(self):
        child_node = LeafNode("b", "child")
        parent_node = ParentNode(None, children=[child_node])
        self.assertRaises(ValueError,parent_node.to_html)
    
    def test_parent_sever_childs(self):
        child_node = LeafNode("b", "child")
        child_node2 = LeafNode("i", "child2")
        child_node3 = LeafNode("b", "child3")
        parent_node = ParentNode("div", [child_node, child_node2, child_node3])
        self.assertEqual(
            parent_node.to_html(),
            "<div><b>child</b><i>child2</i><b>child3</b></div>"
        )
    def test_grandparent_several_parents(self):
        child_node = LeafNode("b", "child")
        parent_node = ParentNode("div", [child_node])
        child_node2 = LeafNode("i", "child2")
        parent_node2 = ParentNode("div", [child_node2])
        grandparent = ParentNode("p", [parent_node, parent_node2])
        self.assertEqual(
            grandparent.to_html(),
            "<p><div><b>child</b></div><div><i>child2</i></div></p>"
        )