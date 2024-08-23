from leafnode import LeafNode
import unittest


class TestingLeaves(unittest.TestCase):
    def test_conv(self):
        node = LeafNode("p", "this is a value!", {"href": "thisisasite.com"})
        input = node.to_html()
        goal = f'<p href="thisisasite.com">this is a value!</p>'
        self.assertEqual(input, goal)

    def test_no_value(self):
        node1 = LeafNode("a", None, {"href": "notasite.com"})
        node1 = node1.to_html()
        self.assertRaises(ValueError)

    def test_no_tag(self):
        node = LeafNode(None, "this is a value", {"idk": "website.com"})
        node = node.to_html()
        goal = "this is a value"
        self.assertFalse(node, goal)


if __name__ == "__main__":
    unittest.main()
