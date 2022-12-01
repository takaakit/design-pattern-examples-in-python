#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from creational_patterns.builder.director import Director
from creational_patterns.builder.plain_text_builder import PlainTextBuilder
from creational_patterns.builder.html_builder import HTMLBuilder

'''
Create documents in HTML format and text format. It is possible to create different documents
in the same construction process.
'''

if __name__ == '__main__':
    input_value = input('Please enter "plain" or "html": ')

    if input_value == 'plain':
        plain_text_builder = PlainTextBuilder()
        directory = Director(builder=plain_text_builder)
        directory.build()
        content = plain_text_builder.get_content()
        print(content)
    elif input_value == 'html':
        html_builder = HTMLBuilder()
        directory = Director(builder=html_builder)
        directory.build()
        file_name = html_builder.get_file_name()
        print(f'{file_name} has been created.')
        print(f'Output File: {os.path.join(os.getcwd(), file_name)}')
    else:
        exit('ERROR: The value is not "plain" or "html".')
