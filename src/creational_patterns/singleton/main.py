#!/usr/bin/env python
# -*- coding: utf-8 -*-
from creational_patterns.singleton.singleton import Singleton

'''
Check whether the same instance is obtained.
'''

if __name__ == '__main__':
    obj_1 = Singleton.get_instance()
    obj_2 = Singleton.get_instance()
    if obj_1 is obj_2:
        print('obj1 and obj2 are the same instance.')
    else:
        print('obj1 and obj2 are different instances.')
