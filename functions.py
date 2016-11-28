#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Functions."""


def my_range(*args):
    """Range function."""
    tuple_length = len(args)
    range_list = []
    if tuple_length == 1:
        x = 0
        while x < args[0]:
            range_list.append(x)
            x += 1
        return range_list
    elif tuple_length == 2:
        x = args[0]
        while x < args[1]:
            range_list.append(x)
            x += 1
        return range_list
    elif tuple_length == 3:
        x = args[0]
        while x < args[1]:
            if x % args[2] == 0:
                range_list.append(x)
            x += 1
        return range_list
    else:
        raise TypeError

"""print(my_range(0, 10, 2, 4))"""


def adt():
    """Advert function."""
    words = {}
    invitation_text = 'Witaj {firstname} {lastname}, zapraszam Cię do skorzystania z {adjective} ofery na {thing}!!!'
    words['firstname'] = str(input('Write firstname: '))
    words['lastname'] = str(input('Write lastname: '))
    words['adjective'] = str(input('Write adjective: '))
    words['thing'] = str(input('Write thing: '))
    print(invitation_text.format(**words))

adt()
