###from textnode import TextNode, TextType
#from delimiters import split_nodes_delimiter


def main():
    copy_static_files("static", "public")
    print("Static files copied successfully!")

import os
import shutil

def copy_static_files(src="static", dest="public"):
    if os.path.exists(dest):
        shutil.rmtree(dest)
        print(f"removed exsisting derectory {dest}")
    os.mkdir(dest)
    print(f"created directory {dest}")

    items = os.listdir(src)
    for item in items:
        src_path = os.path.join(src, item)
        dest_path = os.path.join(dest, item)
        if os.path.isfile(src_path):
            shutil.copy(src_path, dest_path)
            print (f"copied files from {src_path} to {dest_path}")
        else:
            os.mkdir(dest_path)
            print(f"created directory {dest_path}")
            copy_static_files(src_path, dest_path)
            

    

if __name__ == "__main__":
    main()
