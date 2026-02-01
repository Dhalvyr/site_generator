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