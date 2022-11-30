#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from behavioral_patterns.visitor.visitor import Visitor

# ˄


class ListVisitor(Visitor):
    # ˅

    # ˄

    def __init__(self):

        # Currently visited directory
        self.__current_directory = ''

        # ˅
        pass
        # ˄

    # Visit a file
    def visit_file(self, file):
        # ˅
        print(f'{self.__current_directory}/{file.to_string()}')
        # ˄

    # Visit a directory
    def visit_directory(self, directory):
        # ˅
        print(f'{self.__current_directory}/{directory.to_string()}')
        visited_directory = self.__current_directory
        self.__current_directory = f'{self.__current_directory}/{directory.get_name()}'
        for it in iter(directory):
            it.accept(self)
        self.__current_directory = visited_directory
        # ˄

    # ˅

    # ˄


# ˅

# ˄
