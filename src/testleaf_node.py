from leafnode import LeafNode
import unittest


class TestingLeaves(unittest.TestCase):
    def test_conv(self):
        node = LeafNode("p", "this is a value!", {"href": "thisisasite.com"})
        input = node.to_html()
        goal = node.to_html()
        self.assertEqual(input, goal)

    def test_no_value(self):
        node1 = LeafNode("a", None, {"href": "notasite.com"})
        node1 = node1.to_html()
        self.assertRaises(ValueError)

    def test_no_tag(self):
        node = LeafNode(None, "this is a value")
        self.assertEqual(node.to_html(), "this is a value")


if __name__ == "__main__":
    unittest.main()
