from htmlnode import LeafNode, ParentNode
from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    results = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            results.append(node)
        else:
            pieces = node.text.split(delimiter)
            for i in range(len(pieces)):
                if i % 2 == 0:
                    results.append(TextNode(pieces[i], TextType.TEXT))
                else:
                    results.append(TextNode(pieces[i], text_type))

    return results

        
            
                          
    


            