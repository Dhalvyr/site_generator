import os
from copy_static import copy_static_to_public

def main():
    this_dir = os.path.dirname(os.path.abspath(__file__))
    root = os.path.dirname(this_dir)
    static_dir = os.path.join(root, "static")
    public_dir = os.path.join(root, "public")
    copy_static_to_public(static_dir, public_dir)

if __name__ == "__main__":
    main()