#!/usr/bin/env python
# -*- coding: utf-8 -*-
from behavioral_patterns.state.app_safe import AppSafe

'''
Safe security system that the security status changes with time. When you press a button in a dialog,
the message displayed will change depending on whether the time is day or night.
The internal time of the dialog advances one hour for every second of real time.
'''

if __name__ == '__main__':
    app_safe = AppSafe()
