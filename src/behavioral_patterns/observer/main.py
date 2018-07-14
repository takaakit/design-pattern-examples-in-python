#!/usr/bin/env python
# -*- coding: utf-8 -*-
from behavioral_patterns.observer.random_number import RandomNumber
from behavioral_patterns.observer.digit_observer import DigitObserver
from behavioral_patterns.observer.bar_chart_observer import BarChartObserver

# Observers observe objects generating a numerical value and display the value.

if __name__ == '__main__':
    number = RandomNumber()
    digit_observer = DigitObserver()
    bar_chart_observer = BarChartObserver()
    number.add_observer(digit_observer)
    number.add_observer(bar_chart_observer)
    number.generate()
