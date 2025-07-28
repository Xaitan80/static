from textnode import TextNode, Bender  # Import both classes

def main():
    node = TextNode("This is some anchor text", "link", "https://www.boot.dev")
    print(node)  # This will use your __repr__ method to print nicely

if __name__ == "__main__":
    main()  # Call main only if this script is run directly



