#!/usr/bin/env python
# -*- coding: utf-8 -*-
from creational_patterns.prototype.framework.display import Display
from creational_patterns.prototype.framework.manager import Manager
from creational_patterns.prototype.underline_display import UnderlineDisplay
from creational_patterns.prototype.frame_display import FrameDisplay

'''
Display a string enclosed with a frame line, or drawn with an underline. The Client (Main)
registers instances of the Display subclass in the Manager class. When necessary,
the Manager class asks those registered instances to return a clone. The Client (Main)
requires the returned clones to display.
'''

if __name__ == '__main__':
    manager = Manager()

    # Register instances of the "Display" subclass
    emphasis_underline = UnderlineDisplay(underline_char='~')
    manager.register_display(display_name='emphasis', display=emphasis_underline)
    highlight_frame = FrameDisplay(border_char='+')
    manager.register_display(display_name='highlight', display=highlight_frame)
    warning_frame = FrameDisplay(border_char='#')
    manager.register_display(display_name='warning', display=warning_frame)

    # Require to display
    display_1: Display = manager.get_display(display_name='emphasis')
    display_1.show(message='Nice to meet you.')
    display_2: Display = manager.get_display(display_name='highlight')
    display_2.show(message='Nice to meet you.')
    display_3: Display = manager.get_display(display_name='warning')
    display_3.show(message='Nice to meet you.')
