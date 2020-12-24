#!/usr/bin/env python
# -*- coding: utf-8 -*-
from behavioral_patterns.command.app_main import AppMain

'''
Simple drawing application:
* Draw a path with points by dragging the mouse.
* Revert to one previous drawing by pressing the Undo button.
* Erase all drawing by pressing the Clear button.
'''

if __name__ == '__main__':
    app_main = AppMain()
