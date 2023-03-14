#!/usr/bin/env python
# -*- coding: utf-8 -*-
from behavioral_patterns.visitor.directory import Directory
from behavioral_patterns.visitor.file import File
from behavioral_patterns.visitor.list_visitor import ListVisitor

'''
Visitor visits the file system composed of files and directories, and displays a list of files/directories.
'''

if __name__ == '__main__':
    print('Create a file system...')

    bin_dir = Directory(name='bin')
    bin_dir.add(element=File(name='ls', size=20))
    bin_dir.add(element=File(name='mkdir', size=40))

    emily_dir = Directory(name='emily')
    emily_dir.add(element=File(name='homework.doc', size=60))

    james_dir = Directory(name='james')
    james_dir.add(element=File(name='app.exe', size=80))

    home_dir = Directory(name='home')
    home_dir.add(element=emily_dir)
    home_dir.add(element=james_dir)

    root_dir = Directory(name='root')
    root_dir.add(element=bin_dir)
    root_dir.add(element=home_dir)

    root_dir.accept(visitor=ListVisitor())
