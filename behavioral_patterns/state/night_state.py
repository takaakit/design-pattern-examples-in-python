#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from behavioral_patterns.state.state import State

# ˄


class NightState(State):
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
        if 9 <= hour < 17:
            # To avoid circular import of DaytimeState and NightState, write this import here, not at the beginning of this file.
            from behavioral_patterns.state.daytime_state import DaytimeState

            context.change_state(DaytimeState.get_instance())
        # ˄

    def use(self, context):
        # ˅
        context.call_security_guards_room('Emergency: Use a safe at night!')
        # ˄

    def alarm(self, context):
        # ˅
        context.call_security_guards_room('Sound a emergency bell at night')
        # ˄

    def phone(self, context):
        # ˅
        context.record_security_log('Record a night call')
        # ˄

    def to_string(self):
        # ˅
        return '[Night]'
        # ˄

    # ˅

    # ˄


# ˅

# ˄
