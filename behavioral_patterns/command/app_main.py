#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from tkinter import *
from behavioral_patterns.command.history_command import HistoryCommand
from behavioral_patterns.command.painting_canvas import PaintingCanvas
from behavioral_patterns.command.painting_command import PaintingCommand

# ˄


class AppMain(object):
    # ˅

    # ˄

    def __init__(self):

        # Painting history
        self.__history = HistoryCommand()

        self.__canvas = None

        self.__frame = Frame(Tk())

        self.__clear_button = None

        self.__undo_button = None

        # ˅
        self.__frame.pack()
        self.create_widgets()
        self.__frame.mainloop()
        # ˄

    def create_widgets(self):
        # ˅
        self.__frame.master.title('Command Example')

        tk_canvas = Canvas(self.__frame.master, bg = 'white', width = 400.0, height = 300.0)
        tk_canvas.pack(side = BOTTOM)
        tk_canvas.bind('<B1-Motion>', self.on_dragged)

        self.__canvas = PaintingCanvas(tk_canvas)

        self.__undo_button = Button(self.__frame)
        self.__undo_button['text'] = 'Undo'
        self.__undo_button.bind('<Button-1>', self.undo)
        self.__undo_button.pack(side = LEFT)

        self.__clear_button = Button(self.__frame)
        self.__clear_button['text'] = 'Clear'
        self.__clear_button.bind('<Button-1>', self.clear)
        self.__clear_button.pack(side = LEFT)
        # ˄

    def on_dragged(self, event):
        # ˅
        painting_command = PaintingCommand(self.__canvas, event.x, event.y)
        self.__history.add(painting_command)
        painting_command.execute()
        # ˄

    def undo(self, event):
        # ˅
        self.__canvas.clear()
        self.__history.undo()
        self.__history.execute()
        # ˄

    def clear(self, event):
        # ˅
        self.__canvas.clear()
        self.__history.clear()
        # ˄

    # ˅

    # ˄


# ˅

# ˄
