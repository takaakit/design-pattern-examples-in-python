#!/usr/bin/env python
# -*- coding: utf-8 -*-
from creational_patterns.prototype.framework.manager import Manager
from creational_patterns.prototype.underline_display import UnderlineDisplay
from creational_patterns.prototype.frame_display import FrameDisplay

# Display a character string enclosed with a frame line, or drawn with an underline.

if __name__ == '__main__':
    # Create a manager
    manager = Manager()
    emphasis_underline = UnderlineDisplay('~')
    highlight_frame = FrameDisplay('+')
    warning_frame = FrameDisplay('#')
    manager.register_display('emphasis', emphasis_underline)
    manager.register_display('highlight', highlight_frame)
    manager.register_display('warning', warning_frame)

    # Create displays
    display_1 = manager.get_display('emphasis')
    display_1.show('Nice to meet you.')
    display_2 = manager.get_display('highlight')
    display_2.show('Nice to meet you.')
    display_1 = manager.get_display('warning')
    display_1.show('Nice to meet you.')
