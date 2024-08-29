from re import split
from typing import Text
from leafnode import *

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"


class TextNode:
    def __init__(self, text, text_type, url):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other) -> bool:
        if not isinstance(other, TextNode):
            raise Exception("Can only compare with equal types.")

        return (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )

    def text_node_to_html_node(self) -> LeafNode | ValueError:
        match self.text_type:
            case "text":
                return LeafNode(None, self.text, None)
            case "bold":
                return LeafNode("b", self.text, None)
            case "italic":
                return LeafNode("i", self.text, None)
            case "code":
                return LeafNode("code", self.text, None)
            case "link":
                return LeafNode("a", self.text, {"href": self.url})
            case "image":
                return LeafNode("img", "", {"src": self.url, "alt": self.text})
            case _:
                raise ValueError("The type does not exist.")

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
