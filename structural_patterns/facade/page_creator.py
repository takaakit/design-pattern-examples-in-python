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

    __instance = None

    @classmethod
    def get_instance(cls):
        # ˅
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance
        # ˄

    def __init__(self):
        # ˅
        pass
        # ˄

    def create_simple_homepage(self, mail_address, html_file_name):
        # ˅
        address_book = DataLibrary().get_instance().get_properties(os.path.join(os.path.dirname(__file__), 'addressbook.txt'))
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
