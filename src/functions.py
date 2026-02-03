import re
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        old_string= old_node.text.split(delimiter)
        if len(old_string) == 1:
            new_nodes.append(old_node)
        elif len(old_string) % 2 == 0:
            raise Exception("invalid Markdown syntax")
        else:
            for i in range(len(old_string)):
                if i % 2 ==0:
                    new_nodes.append(TextNode(old_string[i], TextType.TEXT))
                else:
                    new_nodes.append(TextNode(old_string[i], text_type))

    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        image = extract_markdown_images(old_node.text)
        if len(image) == 0:
            new_nodes.append(old_node)
            continue
        remaining_text = old_node.text
        for i in range(len(image)):
            old_string = remaining_text.split(f"![{image[i][0]}]({image[i][1]})", 1)
            remaining_text = old_string[1]
            new_nodes.append(TextNode(old_string[0], TextType.TEXT))
            new_nodes.append(TextNode(image[i][0], TextType.IMAGE, image[i][1]))
        if remaining_text != "":
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))
    return new_nodes
        


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        link = extract_markdown_links(old_node.text)
        if len(link) == 0:
            new_nodes.append(old_node)
            continue
        remaining_text = old_node.text
        for i in range(len(link)):
            old_string = remaining_text.split(f"[{link[i][0]}]({link[i][1]})", 1)
            remaining_text = old_string[1]
            new_nodes.append(TextNode(old_string[0], TextType.TEXT))
            new_nodes.append(TextNode(link[i][0], TextType.LINK, link[i][1]))
        if remaining_text != "":
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))
    return new_nodes
