#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from behavioral_patterns.state.state import State

# ˄


class DaytimeState(State):
    # ˅

    # ˄

    __instance = None

    @classmethod
    def get_instance(cls):
        # ˅
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance
        # ˄

    def __init__(self):
        # ˅
        pass
        # ˄

    def set_time(self, context, hour):
        # ˅
        if hour < 9 or 17 <= hour:
            # To avoid circular import of DaytimeState and NightState, write this import here, not at the beginning of this file.
            from behavioral_patterns.state.night_state import NightState

            context.change_state(state=NightState.get_instance())
        # ˄

    def use(self, context):
        # ˅
        context.record_security_log(msg='Use a safe in the daytime')
        # ˄

    def alarm(self, context):
        # ˅
        context.call_security_guards_room(msg='Sound an emergency bell in the daytime')
        # ˄

    def phone(self, context):
        # ˅
        context.call_security_guards_room(msg='Make a normal call in the daytime')
        # ˄

    def to_string(self):
        # ˅
        return '[Daytime]'
        # ˄

    # ˅

    # ˄


# ˅

# ˄
