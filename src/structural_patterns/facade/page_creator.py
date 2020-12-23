#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
import os
from structural_patterns.facade.data_library import DataLibrary
from structural_patterns.facade.html_writer import HtmlWriter

# ˄


class PageCreator(object):
    # ˅

    # ˄

    def create_simple_homepage(self, mail_address, html_file_name):
        # ˅
        address_book = DataLibrary().get_properties('./addressbook.txt')
        user_name = address_book.get('address', mail_address)
        writer = HtmlWriter(html_file_name)
        writer.heading(user_name + '\'s homepage')
        writer.paragraph('Welcome to ' + user_name + '\'s homepage.')
        writer.paragraph('Please email me at this address.')
        writer.mailto(mail_address, user_name)
        writer.close()
        print(html_file_name + ' is created for ' + mail_address + ' (' + user_name + ')')
        print('Output File: ' + os.path.join(os.getcwd(), html_file_name))
        # ˄

    # ˅

    # ˄


# ˅

# ˄
