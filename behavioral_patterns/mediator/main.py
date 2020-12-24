#!/usr/bin/env python
# -*- coding: utf-8 -*-
from behavioral_patterns.mediator.app_login import AppLogin

'''
Show a login dialog for entering a username and password. The dialog has the following elements:
* "Guest" and "Login" radio buttons
* "Username" and "Password" text fields
* "OK" and "Cancel" buttons

And change the editable properties of the elements depending on the state of the radio buttons and text fields.
'''

if __name__ == '__main__':
    app_login = AppLogin()
