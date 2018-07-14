#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from creational_patterns.builder.directory import Directory
from creational_patterns.builder.plain_text_builder import PlainTextBuilder
from creational_patterns.builder.html_builder import HTMLBuilder

# Create documents in HTML format and text format.

def show_usage():
    print('Usage 1: python main.py plain      <- Create a document in plain text.')
    print('Usage 2: python main.py html       <- Create a document in HTML.')

if __name__ == '__main__':
    args = sys.argv
    if len(args) != 2:
        show_usage()
    elif args[1] == 'plain':
        plain_text_builder = PlainTextBuilder()
        directory = Directory(plain_text_builder)
        directory.build()
        content = plain_text_builder.result
        print(content)
    elif args[1] == 'html':
        html_builder = HTMLBuilder()
        directory = Directory(html_builder)
        directory.build()
        file_name = html_builder.result
        print(file_name + ' has been created.')
    else:
        show_usage()
