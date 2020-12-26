#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from behavioral_patterns.state.state import State

# ˄


class DaytimeState(State):
    # ˅

    # ˄

    # Set time
    def set_time(self, context, hour):
        # ˅
        if hour < 9 or 17 <= hour:
            # To avoid circular import of DaytimeState and NightState, write this import here, not at the beginning of this file.
            from behavioral_patterns.state.night_state import NightState

            context.change_state(NightState())
        # ˄

    # Use a safe
    def use_safe(self, context):
        # ˅
        context.record_security_log('Use a safe in the daytime')
        # ˄

    # Sound a emergency bell
    def sound_bell(self, context):
        # ˅
        context.call_security_guards_room('Sound a emergency bell in the daytime')
        # ˄

    # Make a normal call
    def call(self, context):
        # ˅
        context.call_security_guards_room('Make a normal call in the daytime')
        # ˄

    def to_string(self):
        # ˅
        return '[Daytime]'
        # ˄

    # ˅

    # ˄


# ˅

# ˄
