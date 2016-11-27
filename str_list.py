#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Sentence to string list."""


def sentence_to_str_list():
    """Convert sentence to string list."""
    return str(input('Write senetence: ')).split()


def strings_to_replace():
    """String to replace."""
    replace_dist = {}
    for x in range(3):
        find = str(input('Find: '))
        replace = str(input('Replace: '))
        replace_dist[find] = replace
    return replace_dist


def str_list_upper(str_list, replace_dict):
    """Display upper strings from list."""
    find_strings = replace_dict.keys()
    for index, list_item in enumerate(str_list):
        if list_item in find_strings:
            str_list[index] = replace_dict[list_item]
        else:
            str_list[index] = list_item.title()
    print(str_list)


def init():
    """Init function."""
    list_of_strings = sentence_to_str_list()
    replace_dict = strings_to_replace()
    str_list_upper(list_of_strings, replace_dict)

init()
