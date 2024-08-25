import unittest
from parentnode import ParentNode
from leafnode import LeafNode


class ParentNodeTest(unittest.TestCase):
    def test_node(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "this is a Bold value", None),
                LeafNode("i", "this is an Italic value", None),
                LeafNode(None, "Normal Text"),
            ],
            {"href": "thisisawebsite.com", "link": "woagthisworks?"},
        )
        goal = node.to_html()
        print(goal)
        self.assertEqual(node.to_html(), goal)

    def test_parent_nodes(self):
        pass


if __name__ == "__main__":
    unittest.main()
