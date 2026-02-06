from markdown_to_blocks import markdown_to_blocks, BlockType, block_to_block_type
from htmlnode import ParentNode
from functions import text_to_textnodes
from textnode import text_node_to_html_node, TextNode, TextType


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    converted_nodes = []
    for block in blocks:
        converted_nodes.append(block_to_html_node(block))
    return ParentNode("div", converted_nodes)

def block_to_html_node(block):
    type = block_to_block_type(block)
    match type:
        case BlockType.PARAGRAPH:
            paragraph = block.replace("\n", " ")
            children = text_to_children(paragraph)
            return ParentNode("p", children)
        case BlockType.HEADING:
            i = block.split(" ", 1)[0].count("#")
            stripped = block.lstrip("#").lstrip()
            children = text_to_children(stripped)
            return ParentNode(f"h{i}", children)
        case BlockType.CODE:
            text = block[4: -3]
            node = TextNode(text, TextType.TEXT)
            leaf = text_node_to_html_node(node)
            code = ParentNode("code", [leaf])
            return ParentNode("pre", [code])
        case BlockType.QUOTE:
            lines = block.split("\n")
            new_lines = []
            for line in lines:
                new_lines.append(line.lstrip(">").lstrip())
            children = text_to_children(" ".join(new_lines))
            return ParentNode("blockquote", children)
        case BlockType.UNORDERED_LIST:
            list = []
            splitted = block.split("\n")
            for element in splitted:
                children = text_to_children(element.strip("-").lstrip())
                list.append(ParentNode("li", children))
            return ParentNode("ul", list)
        case BlockType.ORDERED_LIST:
            list = []
            splitted = block.split("\n")
            for element in splitted:
                split = element.split(" ", 1)
                children = text_to_children(split[1])
                list.append(ParentNode("li", children))
            return ParentNode("ol", list)
        case _:
            raise ValueError("Invalid block type")
        
def text_to_children(text):
    textnodes = text_to_textnodes(text)
    children = []
    for node in textnodes:
        children.append(text_node_to_html_node(node))
    return children

    