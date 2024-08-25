#!/usr/bin/env python3
from typing import Text
from textnode import TextNode
from htmlnode import *
from leafnode import *


def main():
    node = TextNode("This is some text", "this is the type", "this is some URL")
    print(node)


if __name__ == "__main__":
    main()
