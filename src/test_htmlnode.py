import unittest
from htmlnode import HTMLNode


class TestingHTMLNodes(unittest.TestCase):
    def test_instance(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = HTMLNode("h1", "this is a value", [], props)
        self.assertTrue(isinstance(node, HTMLNode))

    def testeq(self):
        node1 = HTMLNode("a2", "this shit is a val", [], {})
        node2 = node1
        self.assertEqual(node1, node2)

    def test_to_html(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = HTMLNode("h2", "value", [], props)
        converted = node.props_to_html()
        goal = f' href="https://www.google.com" target="_blank"'
        self.assertEqual(converted, goal)

    def test_repr(self):
        node = HTMLNode(" ", " ", [], {})
        print(node)


if __name__ == "__main__":
    unittest.main()
