import re
from htmlnode import LeafNode, ParentNode
from textnode import TextNode, TextType

def extract_markdown_images(text):
    # Regex for markdown image: ![alt](url)
    pattern = r"!\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_links(text):
    # Regex for markdown link: [text](url)
    # But not starting with ! (exclude images)
    pattern = r"(?<!!)(?<!\!)\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    return matches







def split_nodes_image(old_nodes):
    results = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            results.append(node)
        else:
            results.append(node)

    return results

