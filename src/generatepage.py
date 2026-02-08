from markdown_to_html import markdown_to_html_node
from functions import extract_title
import os

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as content:
        from_to_string = content.read()
    with open(template_path, "r") as template:
        template_to_string = template.read()
    content_node = markdown_to_html_node(from_to_string)
    content_html_string = content_node.to_html()
    content_title = extract_title(from_to_string)
    new_html = template_to_string.replace("{{ Title }}", content_title).replace("{{ Content }}", content_html_string)
    dest_directory = os.path.dirname(dest_path)
    if not os.path.exists(dest_directory):
        os.makedirs(dest_directory)
    with open(dest_path, "w") as file:
        file.write(new_html)
