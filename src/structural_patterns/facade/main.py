#!/usr/bin/env python
# -*- coding: utf-8 -*-
from structural_patterns.facade.page_creator import PageCreator

# Create a simple homepage.

if __name__ == '__main__':
    PageCreator().create_simple_homepage('emily@example.com', 'Homepage.html')
