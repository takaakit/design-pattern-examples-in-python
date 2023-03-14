#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
from time import sleep
from behavioral_patterns.observer.number_subject import NumberSubject
from behavioral_patterns.observer.digit_observer import DigitObserver
from behavioral_patterns.observer.bar_chart_observer import BarChartObserver

'''
Observers observe a Subject object holding a numerical value and display the value.
The display formats are digits and bar charts.
'''

if __name__ == '__main__':
    number_subject = NumberSubject()
    number_subject.attach(observer=DigitObserver(number_subject))
    number_subject.attach(observer=BarChartObserver(number_subject))

    for _ in range(0, 20):
        number_subject.value = random.randrange(50)
        sleep(0.2)
