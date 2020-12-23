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

    bin_dir = Directory('bin')
    bin_dir.add(File('ls', 20))
    bin_dir.add(File('mkdir', 40))

    emily_dir = Directory('emily')
    emily_dir.add(File('homework.doc', 60))

    james_dir = Directory('james')
    james_dir.add(File('app.exe', 80))

    home_dir = Directory('home')
    home_dir.add(emily_dir)
    home_dir.add(james_dir)

    root_dir = Directory('root')
    root_dir.add(bin_dir)
    root_dir.add(home_dir)

    root_dir.accept(ListVisitor())
