#!/usr/bin/env python
# -*- coding: utf-8 -*-
from structural_patterns.decorator.message_display import MessageDisplay
from structural_patterns.decorator.side_frame import SideFrame
from structural_patterns.decorator.full_frame import FullFrame

# Display a character string with a decorative frame.

if __name__ == '__main__':
    display_a = MessageDisplay('Nice to meet you.')
    display_a.show()

    display_b = SideFrame(display_a, '!')
    display_b.show()

    display_c = FullFrame(display_b)
    display_c.show()

    display_d = SideFrame(
        FullFrame(
            FullFrame(
                SideFrame(
                    SideFrame(
                        FullFrame(
                            MessageDisplay('See you again.')
                        ),
                        '#'
                    ),
                    '#'
                )
            )
        ),
        '#'
    )
    display_d.show()
