#!/usr/bin/env python3
"""General testing class for the TextNode."""

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

import unittest
from textnode import *
from leafnode import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        """Test if both obj are equal"""
        node = TextNode("this is some text", "bold", "no url")
        node2 = TextNode("this is some text", "bold", "no url")
        self.assertEqual(node, node2)

    def test_noneq(self):
        """Test if both objects are not equal"""
        node = TextNode("This is some text", "bold", "no url")
        node2 = TextNode("This is not some text", "bold", "url")
        self.assertNotEqual(node, node2)

    def test_none(self):
        """Test when the object properties are None"""
        node = TextNode(None, None, None)
        node2 = TextNode(None, None, None)
        self.assertEqual(node, node2)

    def test_conversion_raw_text(self):
        node = TextNode("This is some text", "text", None)
        goal = node.text_node_to_html_node().to_html()
        print(node, "\n", goal)
        self.assertEqual(node.text_node_to_html_node().to_html(), goal)

    def test_conversion_img_tag(self):
        node = TextNode("thisisthevalue", "image", "thisisthelink.com")
        goal = node.text_node_to_html_node().to_html()
        print(node, "\n", goal)
        self.assertEqual(node.text_node_to_html_node().to_html(), goal)

    def test_conversion_code(self):
        node = TextNode("This is a value", "code", "link.js")
        goal = node.text_node_to_html_node().to_html()
        print(node, "\n", goal)
        self.assertEqual(node.text_node_to_html_node().to_html(), goal)


if __name__ == "__main__":
    unittest.main()
