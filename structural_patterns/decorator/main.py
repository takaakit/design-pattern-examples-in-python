#!/usr/bin/env python
# -*- coding: utf-8 -*-
from structural_patterns.decorator.display import Display
from structural_patterns.decorator.message_display import MessageDisplay
from structural_patterns.decorator.side_frame import SideFrame
from structural_patterns.decorator.full_frame import FullFrame

'''
Display a string with decorative frames. The frames can be combined arbitrarily.
'''

if __name__ == '__main__':
    display_a: Display = MessageDisplay(message='Nice to meet you.')
    display_a.show()

    display_b: Display = SideFrame(display=MessageDisplay(message='Nice to meet you.'), frame_char='!')
    display_b.show()

    display_c: Display = FullFrame(display=SideFrame(display=MessageDisplay(message='Nice to meet you.'), frame_char='!'))
    display_c.show()
