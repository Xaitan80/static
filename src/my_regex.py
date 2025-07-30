import re

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
    i = 0
    while i < len(old_nodes):
        if old_nodes[i:i+2] == "![":
            alt_start = i + 2
            alt_end = old_nodes.find("]", alt_start)
            if alt_end == -1:
                break
            if old_nodes[alt_end + 1] != "(":
                i = alt_end + 1
                continue
            url_start = alt_end + 2
            url_end = old_nodes.find(")", url_start)
            if url_end == -1:
                break
                alt_text = old_nodes[alt_start:alt_end]
                url = text[url_start:url_end]
                results.append((alt_text, url))
                i = url_end + 1
            else:
                i += 1
        return results