#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from tkinter import *
from behavioral_patterns.mediator.colleague_button import ColleagueButton
from behavioral_patterns.mediator.colleague_radio_button import ColleagueRadioButton
from behavioral_patterns.mediator.colleague_text_field import ColleagueTextField
from behavioral_patterns.mediator.mediator import Mediator

# ˄


class AppLogin(Mediator):
    # ˅

    # ˄

    def __init__(self):

        self.val = None

        self.__radio_login = None

        self.__radio_guest = None

        self.__text_username = None

        self.__text_password = None

        self.__button_ok = None

        self.__button_cancel = None

        self.__master = Tk()

        # ˅
        self.__master.title('Mediator Example')

        self.create_colleagues()
        self.set_mediators()

        self.colleague_changed()

        self.__master.mainloop()
        # ˄

    # Change enable/disable of the Colleagues when notified from the Mediators.
    def colleague_changed(self):
        # ˅
        if self.__button_ok.is_pressed() or self.__button_cancel.is_pressed():
            self.__master.quit()
        else:
            if self.__radio_guest.is_selected():      # Guest mode
                self.__text_username.set_activation(False)
                self.__text_password.set_activation(False)
                self.__button_ok.set_activation(True)
            else:                                   # Login mode
                self.__text_username.set_activation(True)
                self.__text_password.set_activation(True)

                # Judge whether the changed Colleage is enabled or disabled
                if self.__text_username.is_empty() == False and self.__text_password.is_empty() == False:
                    self.__button_ok.set_activation(True)
                else:
                    self.__button_ok.set_activation(False)
        # ˄

    def create_colleagues(self):
        # ˅
        radio_button_frame = Frame(self.__master)
        radio_button_frame.pack(anchor = W)

        self.val = IntVar()
        self.val.set(0)

        radio_button_guest = Radiobutton(
            radio_button_frame,
            text = 'Guest',
            variable = self.val,
            value = 0)
        radio_button_guest.grid(row = 0, column = 0)
        self.__radio_guest = ColleagueRadioButton(radio_button_guest)

        radio_button_login = Radiobutton(
            radio_button_frame,
            text = 'Login',
            variable = self.val,
            value = 1)
        radio_button_login.grid(row = 0, column = 1)
        self.__radio_login = ColleagueRadioButton(radio_button_login)

        text_field_frame = Frame(self.__master)
        text_field_frame.pack()

        label_username = Label(text_field_frame, text = 'Username:')
        label_username.grid(row = 0, column = 0)

        label_password = Label(text_field_frame, text = 'Password:')
        label_password.grid(row = 1, column = 0)

        text_username = Entry(text_field_frame, width = 20)
        text_username.grid(row = 0, column = 1)
        self.__text_username = ColleagueTextField(text_username)

        text_password = Entry(text_field_frame, width = 20, show = '*')
        text_password.grid(row = 1, column = 1)
        self.__text_password = ColleagueTextField(text_password)

        button_frame = Frame(self.__master)
        button_frame.pack(anchor = E)

        button_ok = Button(button_frame, text = 'OK')
        button_ok.grid(row = 0, column = 0)
        self.__button_ok = ColleagueButton(button_ok)

        button_cancel = Button(button_frame, text = 'Cancel')
        button_cancel.grid(row = 0, column = 1)
        self.__button_cancel = ColleagueButton(button_cancel)
        # ˄

    # Set mediators
    def set_mediators(self):
        # ˅
        self.__radio_login.mediator = self
        self.__radio_guest.mediator = self
        self.__text_username.mediator = self
        self.__text_password.mediator = self
        self.__button_ok.mediator = self
        self.__button_cancel.mediator = self
        # ˄

    # ˅

    # ˄


# ˅

# ˄
