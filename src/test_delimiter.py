from textnode import *
from delimiter_finder import *
import unittest


class TestingGround(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", text_type_text, None)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        print(new_nodes)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text, None),
                TextNode("bolded", text_type_bold, None),
                TextNode(" word", text_type_text, None),
            ],
            new_nodes,
        )

    def test_extracting_links(self):
        text = "This is an example of a ![alt text within](https://i.imgur.com/jh3h4hHN.jpeg)"
        goal = extract_markdown_images(text)
        self.assertEqual(extract_markdown_images(text), goal)

    def test_img_split_nodes(self):
        node = TextNode(
            "This is an example with ![alt text](https://i.imgur.com/hHN4Hhnf.jpeg) inside of it",
            text_type_text,
            None,
        )
        goal = split_img_nodes([node])
        print(goal)
        self.assertListEqual(split_img_nodes([node]), goal)

    def test_link_split_nodes(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            text_type_text,
            None,
        )
        goal = split_link_nodes([node])
        print(goal)
        self.assertListEqual(split_link_nodes([node]), goal)

    def test_final_func(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        goal = text_to_text_nodes(text)
        print(goal)
        self.assertListEqual(text_to_text_nodes(text), goal)

    def test_markdown_to_blocks(self):
        text = f"# This is some text \n\n This is another block of text \n\n * This is the first list item in a list block * This is a list item * This is another list item "
        goal = markdown_to_blocks(text)
        print(goal)
        self.assertListEqual(markdown_to_blocks(text), goal)
