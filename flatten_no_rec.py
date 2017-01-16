#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Flatten no recursive function."""


def flatten(nested_list):
    """Flatten function."""
    convert = True
    stack = []
    flatten_list = []
    current_list = nested_list
    while convert:
        x = 0
        for el in current_list:
            if type(el) is list:
                buffer_list = current_list[x]
                current_list.pop(x)
                stack.append(current_list)
                stack.append(buffer_list)
                x = 0
                break
            else:
                flatten_list.append(el)
                current_list.pop(x)
            x = x + 1
        if len(stack) > 0:
            current_list = stack.pop()
        else:
            convert = False
    print(flatten_list)

flatten([[[[[[[[[['a'], 'b']]], 'c']]], 'd']], 'e'])
