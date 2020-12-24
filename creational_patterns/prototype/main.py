#!/usr/bin/env python
# -*- coding: utf-8 -*-
from creational_patterns.prototype.framework.manager import Manager
from creational_patterns.prototype.underline_display import UnderlineDisplay
from creational_patterns.prototype.frame_display import FrameDisplay

'''
Display a string enclosed with a frame line, or drawn with an underline. The client("Main") registers instances of the "Display" subclass in the "Manager" class. When necessary, the "Manager" class asks those registered instances to return a clone. The client("Main") requires the returned clones to display.
'''

if __name__ == '__main__':
    manager = Manager()

    # Register instances of the "Display" subclass
    emphasis_underline = UnderlineDisplay('~')
    manager.register_display('emphasis', emphasis_underline)
    highlight_frame = FrameDisplay('+')
    manager.register_display('highlight', highlight_frame)
    warning_frame = FrameDisplay('#')
    manager.register_display('warning', warning_frame)

    # Require to display
    display_1 = manager.get_display('emphasis')
    display_1.show('Nice to meet you.')
    display_2 = manager.get_display('highlight')
    display_2.show('Nice to meet you.')
    display_1 = manager.get_display('warning')
    display_1.show('Nice to meet you.')
