#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Read persons from file."""

import re

def get_dictionary_from_file():
    """Read dat from file and display like dictionary."""
    with open('persons.txt', 'r') as persons_file:
        data_from_file = persons_file.read()
    splited_data = data_from_file.split("\n")
    persons = {}
    for data in splited_data:
        matched = re.match(
            '^[\d]+. ([a-zA-Z0-9-Ã©]+ ?[a-zA-Z0-9-Ã©]+? ?[a-zA-Z0-9-Ã©]+?) has ([a-z-]+,? ?[a-z-]+?) and is (\d+) cm tall$',
            data)
        if matched:
            person = {}
            person['eye_color'] = matched.group(2)
            person['height'] = matched.group(3)
            persons[matched.group(1)] = person
    return persons


def write_persons_to_files():
    """Write persons to files."""
    with open('persons.txt', 'r') as persons_file:
        data_from_file = persons_file.read()
    splited_data = data_from_file.split("\n")
    for data in splited_data:
        matched = re.match(
            '^[\d]+. ([a-zA-Z0-9-Ã©]+ ?[a-zA-Z0-9-Ã©]+? ?[a-zA-Z0-9-Ã©]+?) has ([a-z-]+,? ?[a-z-]+?) and is (\d+) cm tall$',
            data)
        if matched:
            if int(matched.group(3)) > 200:
                with open('hero_200_plus.txt', 'a') as persons_plus:
                    persons_plus.write(data + "\n")
            else:
                with open('hero_short.txt', 'a') as persons_short:
                    persons_short.write(data + "\n")


def colors_height():
    """Function colors_height."""
    persons = get_dictionary_from_file()
    colors = set()
    for key, value in persons.items():
        colors.add(value['eye_color'])
    medium_height = {}
    for color in colors:
        medium_height[color] = {'count': 0, 'sum': 0}
    for key, value in persons.items():
        medium_height[value['eye_color']]['count'] += 1
        medium_height[value['eye_color']]['sum'] += int(value['height'])
    for key, value in medium_height.items():
        with open('medium_height.txt', 'a') as colors_height_file:
            tmp = "Średni wzrost osoby z kolorem oczu %s wynosi %0.2f cm.\n"
            colors_height_file.write(tmp % (key, value['sum'] / value['count']))


def colors_height_translate():
    """Function translate english colors to polish."""
    colors_translations = {
        'pink': 'różowy',
        'red': 'czerwony',
        'blue': 'niebieski',
        'green': 'zielony',
        'yellow': 'żółty',
        'gray': 'szary',
        'unknown': 'nieznany',
        'orange': 'pomarańczowy',
        'hazel': 'piwny',
        'gold': 'złoty',
        'brown': 'brązowy',
        'black': 'czarny'}
    with open('medium_height.txt', 'r') as data_file:
        data = data_file.read()
    for key, value in colors_translations.items():
        data = re.sub(re.compile(key), value, data)
    with open('medium_height_translated.txt', 'w') as data_translated_file:
        data_translated_file.write(data)

colors_height_translate()
