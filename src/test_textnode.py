#!/usr/bin/env python3
"""General testing class for the TextNode."""

import cProfile
import unittest
from textnode import TextNode


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


if __name__ == "__main__":
    unittest.main()
