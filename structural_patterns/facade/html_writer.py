#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅

# ˄


class HtmlWriter(object):
    # ˅
    
    # ˄

    def __init__(self, html_file_name):

        self.__writer = open(html_file_name, 'w')

        # ˅
        pass
        # ˄

    # Write a title
    def heading(self, title):
        # ˅
        self.__writer.write('<html>')
        self.__writer.write('<head><title>' + title + '</title></head>')
        self.__writer.write('<body>\n')
        self.__writer.write('<h1>' + title + '</h1>\n')
        # ˄

    # Write a paragraph
    def paragraph(self, message):
        # ˅
        self.__writer.write('<p>' + message + '</p>\n')
        # ˄

    # Write a link
    def anchor(self, url, text):
        # ˅
        self.paragraph('<a href=\"' + url + '\">' + text + '</a>')
        # ˄

    # Write a mail address
    def mailto(self, mail_address, user_name):
        # ˅
        self.anchor('mailto:' + mail_address, user_name)
        # ˄

    def close(self):
        # ˅
        self.__writer.write('</body>')
        self.__writer.write('</html>\n')
        self.__writer.close()
        # ˄

    # ˅
    
    # ˄


# ˅

# ˄
