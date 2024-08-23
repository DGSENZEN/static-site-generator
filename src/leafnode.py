from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        props_html = ""
        if self.value is None:
            return ValueError
        props_html = self.props_to_html()
        if self.tag is None:
            return self.tag

        return f"<{self.tag}{props_html}>{self.value}</{self.tag}>"
