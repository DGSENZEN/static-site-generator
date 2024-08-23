#!/usr/bin/env python3
from textnode import TextNode


def main():
    node = TextNode("This is some text", "this is the type", "this is some URL")
    print(node)


if __name__ == "__main__":
    main()
