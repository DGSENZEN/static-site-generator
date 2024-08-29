from delimiter_finder import *

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_ulist = "ulist"
block_type_olist = "olist"


def block_to_block_type(block):
    lines = block.split("\n")
    if (
        block.startswith("###### ")
        or block.startswith("##### ")
        or block.startswith("#### ")
        or block.startswith("### ")
        or block.startswith("## ")
        or block.startswith("# ")
    ):
        return block_type_heading
    elif block.startswith("```") and block.endswith("```"):
        return block_type_code
    elif block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return block_type_paragraph
        return block_type_quote
    elif block.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return block_type_paragraph
        return block_type_ulist
    elif block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return block_type_paragraph
        return block_type_ulist
    elif block.startswith("1."):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}."):
                return block_type_paragraph
            i += 1
        return block_type_olist
    return block_type_paragraph
