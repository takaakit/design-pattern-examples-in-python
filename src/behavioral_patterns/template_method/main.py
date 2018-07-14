#!/usr/bin/env python
# -*- coding: utf-8 -*-
from behavioral_patterns.template_method.char_display import CharDisplay
from behavioral_patterns.template_method.string_display import StringDisplay

# Display the character and string repeatedly 5 times.

if __name__ == '__main__':
    display_1 = CharDisplay('H')                     # Create an instance of the CharDisplay
    display_2 = StringDisplay('Hello world.')        # Create an instance of the StringDisplay
    display_3 = StringDisplay('Nice to meet you.')   # Create an instance of the StringDisplay

    # Any instance can be called with the same method name
    display_1.output()
    display_2.output()
    display_3.output()
