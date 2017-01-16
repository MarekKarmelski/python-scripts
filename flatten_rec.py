#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Flatten recursive function."""


def get_flat_list(nested_list, flat_list=[]):
    """Get flat list function."""
    for el in nested_list:
        if type(el) is list:
            flat_list = get_flat_list(el, flat_list)
        else:
            flat_list.append(el)
    return flat_list


def flatten(nested_list):
    """Flatten function."""
    print(get_flat_list(nested_list, []))


flatten([[[[[[[[[['a'], 'b']]], 'c']]], 'd']], 'e'])
