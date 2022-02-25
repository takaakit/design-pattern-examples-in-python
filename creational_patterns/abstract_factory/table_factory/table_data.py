#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from creational_patterns.abstract_factory.factory.data import Data

# ˄


class TableData(Data):
    # ˅

    # ˄

    def __init__(self, name):
        # ˅
        super().__init__(name)
        # ˄

    def to_html(self):
        # ˅
        buffer = list()
        buffer.append('<td><table width="100%" border="2">\n')
        buffer.append('<tr><td bgcolor="#00CC00" align="center" colspan="' + str(len(self.items)) + '"><b>' + self.name + '</b></td></tr>\n')
        buffer.append('<tr>\n')
        for item in self.items:
            buffer.append(item.to_html())
        buffer.append('</tr>\n')
        buffer.append('</table></td>\n')
        return ''.join(buffer)
        # ˄

    # ˅

    # ˄


# ˅

# ˄
