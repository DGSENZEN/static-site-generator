import re
from textnode import TextNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_img = "image"


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text, None))
            else:
                split_nodes.append(TextNode(sections[i], text_type, None))
        new_nodes.extend(split_nodes)
    return new_nodes


def extract_markdown_images(text):
    tup_lst = []
    pattern = r"!\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    for alt_text, url in matches:
        tup_lst.append((alt_text, url))
    return tup_lst


def extract_markdown_links(text):
    tup_lst = []
    pattern = r"(?<!!)\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    for alt_text, url in matches:
        tup_lst.append((alt_text, url))
    return tup_lst


def split_img_nodes(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        extracted_tup = extract_markdown_images(old_node.text)
        if not extracted_tup:
            new_nodes.append(old_node)
            continue
        remaining_text = old_node.text
        for alt_text, url in extracted_tup:
            parts = remaining_text.split(f"[{alt_text}]({url})")
            if parts[0]:
                new_nodes.append(TextNode(parts[0], text_type_text, None))
            new_nodes.append(TextNode(alt_text, text_type_img, url))
            remaining_text = parts[1] if len(parts) > 1 else ""

        if remaining_text:
            new_nodes.append(TextNode(remaining_text, text_type_text, None))
    return new_nodes


def split_link_nodes(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        extracted_tup = extract_markdown_links(old_node.text)
        if not extracted_tup:
            new_nodes.append(old_node)
            continue
        remaining_text = old_node.text
        for alt_text, url in extracted_tup:
            parts = remaining_text.split(f"[{alt_text}]({url})")
            if parts[0]:
                new_nodes.append(TextNode(parts[0], text_type_text, None))
            new_nodes.append(TextNode(alt_text, text_type_link, url))
            remaining_text = parts[1] if len(parts) > 1 else ""

        if remaining_text:
            new_nodes.append(TextNode(remaining_text, text_type_text, None))
    return new_nodes


def text_to_text_nodes(text):
    new_nodes = [TextNode(text, text_type_text, None)]

    new_nodes = split_nodes_delimiter(new_nodes, "**", text_type_bold)  # bold

    new_nodes = split_nodes_delimiter(new_nodes, "*", text_type_italic)  # italics

    new_nodes = split_nodes_delimiter(new_nodes, "`", text_type_code)

    new_nodes = split_img_nodes(new_nodes)
    new_nodes = split_link_nodes(new_nodes)

    return new_nodes


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks
