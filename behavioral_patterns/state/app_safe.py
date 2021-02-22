#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
import threading
from time import sleep
from tkinter import *
from tkinter.scrolledtext import *
from behavioral_patterns.state.context import Context
from behavioral_patterns.state.daytime_state import DaytimeState

# ˄


class AppSafe(Context):
    # ˅

    # ˄

    def __init__(self):

        # Current state
        self.__state = DaytimeState()

        self.__master = Tk()

        # Current time
        self.__text_time = None

        # Display of security center
        self.__text_message = None

        # ˅
        self.__master.title('State Example')

        time_frame = Frame(self.__master)
        time_frame.pack(anchor = W)

        text_time = Entry(time_frame, width = 20)
        text_time.grid(sticky = W)
        self.__text_time = text_time

        message_frame = Frame(self.__master)
        message_frame.pack()

        text_message = ScrolledText(message_frame, height = 8, wrap = None)
        text_message.grid(sticky = N + E + W + S)
        self.__text_message = text_message

        button_frame = Frame(self.__master)
        button_frame.pack()

        button_use = Button(button_frame, text = 'Use')
        button_use.bind("<Button-1>", self.__use_safe)           # Use button pressed
        button_use.grid(row = 0, column = 0)

        button_alarm = Button(button_frame, text = 'Alarm')
        button_alarm.bind("<Button-1>", self.__sound_bell)       # Alarm button pressed
        button_alarm.grid(row = 0, column = 1)

        button_phone = Button(button_frame, text = 'Phone')
        button_phone.bind("<Button-1>", self.__call)             # Phone button pressed
        button_phone.grid(row = 0, column = 2)

        button_exit = Button(button_frame, text = 'Exit')
        button_exit.bind("<Button-1>", self.__exit)              # Exit button pressed
        button_exit.grid(row = 0, column = 3)

        count_time_thread = threading.Thread(target = self.count_time)
        count_time_thread.setDaemon(True)
        count_time_thread.start()

        self.__master.mainloop()
        # ˄

    # Set time
    def set_time(self, hour):
        # ˅
        clock_string = 'Current Time : '
        if hour < 10:
            clock_string += '0' + str(hour) + ':00'
        else:
            clock_string += str(hour) + ':00'
        print(clock_string)
        self.__text_time.delete(0, 'end')
        self.__text_time.insert(0, clock_string)
        self.__state.set_time(self, hour)
        # ˄

    # Change state
    def change_state(self, state):
        # ˅
        print('The state changed from ' + self.__state.to_string() + ' to ' + state.to_string())
        self.__state = state
        # ˄

    # Call a security guard room
    def call_security_guards_room(self, msg):
        # ˅
        self.__text_message.insert('end', 'call! ' + msg + '\n')
        self.__text_message.yview_moveto(1)     # Scroll to the bottom
        # ˄

    # Record security log
    def record_security_log(self, msg):
        # ˅
        self.__text_message.insert('end', 'record ... ' + msg + '\n')
        self.__text_message.yview_moveto(1)     # Scroll to the bottom
        # ˄

    def count_time(self):
        # ˅
        while True:
            for hour in range(0, 23, 1):
                self.set_time(hour)      # Set the time
                sleep(1)
        # ˄

    def __use_safe(self, event):
        # ˅
        self.__state.use_safe(self)
        # ˄

    def __sound_bell(self, event):
        # ˅
        self.__state.sound_bell(self)
        # ˄

    def __call(self, event):
        # ˅
        self.__state.call(self)
        # ˄

    def __exit(self, event):
        # ˅
        self.__master.quit()
        # ˄

    # ˅
    
    # ˄


# ˅

# ˄
