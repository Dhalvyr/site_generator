import os
from copy_static import copy_static_to_public
from generatepage import generate_page

def main():
    this_dir = os.path.dirname(os.path.abspath(__file__))
    root = os.path.dirname(this_dir)
    static_dir = os.path.join(root, "static")
    public_dir = os.path.join(root, "public")
    copy_static_to_public(static_dir, public_dir)
    content_dir = os.path.join(root, "content/index.md")
    template_dir = os.path.join(root, "template.html")
    target_dir = os.path.join(root, "public/index.html")
    generate_page(content_dir, template_dir, target_dir)

if __name__ == "__main__":
    main()