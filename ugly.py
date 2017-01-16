#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Ugly function."""


def ugly(number):
    """Ugly function."""
    if isinstance(number, int):
        if number is 1:
            return True
        elif number % 2 is 0:
            return True
        elif number % 3 is 0:
            return True
        elif number % 5 is 0:
            return True
        else:
            return False
    else:
        print('Number must by an integer.')

is_ugly = ugly(12)
print(is_ugly)
