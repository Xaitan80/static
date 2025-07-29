from textnode import TextNode, TextType
#from delimiters import split_nodes_delimiter


def main():
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(node)


main()
