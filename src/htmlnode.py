class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Not implemented yet.")

    def props_to_html(self):
        property_html = ""
        if self.props is None:
            return ""
        for prop in self.props:
            property_html += f' {prop}="{self.props[prop]}"'
        return property_html

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
