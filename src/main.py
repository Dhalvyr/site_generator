import os
import sys
from copy_static import copy_static_to_public
from generatepage import generate_pages_recursive

def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    this_dir = os.path.dirname(os.path.abspath(__file__))
    root = os.path.dirname(this_dir)
    static_dir = os.path.join(root, "static")
    public_dir = os.path.join(root, "docs")
    copy_static_to_public(static_dir, public_dir)
    content_dir = os.path.join(root, "content")
    template_dir = os.path.join(root, "template.html")
    target_dir = os.path.join(root, "docs")
    generate_pages_recursive(content_dir, template_dir, target_dir, basepath)

if __name__ == "__main__":
    main()
