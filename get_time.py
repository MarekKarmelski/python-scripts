#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re


"""Get time."""


def get_time(time_in_string, type='s'):
    """Get time."""
    matched = re.match('^(\d{1,2}):(\d{2}):(\d{2})$', time_in_string)
    if matched is None:
        print('Incorrect time format. Correct time format is HH:MM:SS')
        return False
    if type not in ['s', 'm', 'h']:
        print(
            'Incorrect type format. Correct type is: s - seconds, m - minutes, h - hours'
        )
        return False

    hours = int(matched.group(1))
    minutes = int(matched.group(2))
    seconds = int(matched.group(3))

    if minutes > 59 or seconds > 59:
        print('Minutes or seconds ar bigger then 59')
        return False
    time_in_seconds = hours * 3600 + minutes * 60 + seconds
    if type is 's':
        print(time_in_seconds)
    elif type is 'm':
        converted = float(time_in_seconds) / 60
        if seconds > 0:
            print(converted)
        else:
            print(int(converted))
    elif type is 'h':
        converted = float(time_in_seconds) / 3600
        if minutes > 0 or seconds > 0:
            print(converted)
        else:
            print(int(converted))

get_time('2:00:00', 'm')
