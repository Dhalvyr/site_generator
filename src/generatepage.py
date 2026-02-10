from markdown_to_html import markdown_to_html_node
from functions import extract_title
from pathlib import Path
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

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    directories = os.listdir(dir_path_content)
    for directory in directories:
        full_path = os.path.join(dir_path_content, directory)
        target_path = os.path.join(dest_dir_path, directory)
        if os.path.isfile(full_path) and directory.endswith(".md"):
            generate_page(full_path, template_path, str(Path(target_path).with_suffix(".html")))
        elif os.path.isdir(full_path):
            generate_pages_recursive(full_path, template_path, target_path)