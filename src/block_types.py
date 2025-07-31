from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"
    


def block_to_block_type(block):
    # Check for HEADING
    if block.startswith("#"):
        count = 0
        for char in block:
            if char == '#':
                count += 1
            elif char == ' ':
                break  # stop counting if there are no more #
            else:
                # invalid input
                count = 0
                break

        if 1 <= count <= 6:
            return BlockType.HEADING

    # Check for CODE
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE

    # Check for QUOTE
    lines = block.splitlines()
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE

    # Check for unordered list
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST

    # Check for ordered list
    for i, line in enumerate(lines, start=1):
        if not line.startswith(f"{i}. "):
            break
    else:
        # only reached if for loop was NOT broken
        return BlockType.ORDERED_LIST

    # If none matched, return paragraph
    return BlockType.PARAGRAPH

        
        
        
            
        
        
            
        

    
    
    
    
    
    
    
    
            
