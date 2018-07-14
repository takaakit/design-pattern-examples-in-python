#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from behavioral_patterns.state.state import State

# ˄


class NightState(State):
    # ˅

    # ˄

    # Set time
    def set_time(self, context, hour):
        # ˅
        if 9 <= hour and hour < 17:
            from behavioral_patterns.state.daytime_state import DaytimeState
            context.change_state(DaytimeState())
        # ˄

    # Use a safe
    def use_safe(self, context):
        # ˅
        context.call_security_guards_room('Emergency: Use a safe at night!')
        # ˄

    # Sound a emergency bell
    def sound_bell(self, context):
        # ˅
        context.call_security_guards_room('Sound a emergency bell at night')
        # ˄

    # Make a normal call
    def call(self, context):
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
