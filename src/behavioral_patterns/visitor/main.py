#!/usr/bin/env python
# -*- coding: utf-8 -*-
from behavioral_patterns.visitor.directory import Directory
from behavioral_patterns.visitor.file import File
from behavioral_patterns.visitor.list_visitor import ListVisitor

# Visitors visit a file system composed of files and directories, and displays a list of files/directories.

if __name__ == '__main__':
    print('Create a file system...')
    root_dir = Directory('root')
    home_dir = Directory('home')
    bin_dir = Directory('bin')
    etc_dir = Directory('etc')
    emily_dir = Directory('emily')
    james_dir = Directory('james')
    olivia_dir = Directory('olivia')

    root_dir.add(home_dir)
    root_dir.add(bin_dir)
    root_dir.add(etc_dir)

    bin_dir.add(File('ls', 100))
    bin_dir.add(File('mkdir', 50))
    home_dir.add(emily_dir)
    home_dir.add(james_dir)
    home_dir.add(olivia_dir)

    emily_dir.add(File('homework.doc', 40))
    james_dir.add(File('homework.doc', 50))
    james_dir.add(File('app.exe', 60))
    olivia_dir.add(File('homework.doc', 70))
    olivia_dir.add(File('app.exe', 80))
    olivia_dir.add(File('tips.html', 90))

    root_dir.accept(ListVisitor())
