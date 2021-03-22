#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from behavioral_patterns.command.command import Command

# ˄


# Holder of the past commands
class HistoryCommand(Command):
    # ˅

    # ˄

    def __init__(self):

        # A set of past commands
        self.__past_commands = []

        # ˅
        pass
        # ˄

    def execute(self):
        # ˅
        for past_command in self.__past_commands:
            past_command.execute()
        # ˄

    def add(self, cmd):
        # ˅
        self.__past_commands.append(cmd)
        # ˄

    # Delete the last command
    def undo(self):
        # ˅
        if len(self.__past_commands) != 0:
            self.__past_commands.pop()
        # ˄

    # Delete all past commands
    def clear(self):
        # ˅
        self.__past_commands.clear()
        # ˄

    # ˅

    # ˄


# ˅

# ˄
