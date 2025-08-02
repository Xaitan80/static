import os
import shutil
from markdown_blocks import markdown_to_html_node



def main():
    copy_static_files("static", "public")
    print("Static files copied successfully!")
    generate_page("content/index.md", "template.html", "public/index.html")

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

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    raise Exception("No level-one header found")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as f:
        markdown_content = f.read()
    with open(template_path, "r") as f:
        template = f.read()
        
    title = extract_title(markdown_content)
    html = markdown_to_html_node(markdown_content).to_html()
    final_html = template.replace("{{ Title }}", title).replace("{{ Content }}", html)

    #check the filepath
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(final_html)






            

    

if __name__ == "__main__":
    main()
