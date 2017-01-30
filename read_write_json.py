#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""JSON data."""

import json


def get_json_data_from_file(file_path):
    """Get JSON data from file."""
    with open(file_path) as json_file:
        data = json.load(json_file)
    return data


def save_by_gender(json_data):
    """Save persons by gender."""
    filtered_data = list(filter(lambda a: a['gender'] != 'unknown', json_data))
    men = list(filter(lambda a: a['gender'] == 'male', filtered_data))
    women = list(filter(lambda a: a['gender'] == 'female', filtered_data))
    for m in men:
        with open('sw_men.txt', 'a') as men_file:
            men_file.write(m['name'] + "\n")
    for w in women:
        with open('sw_women.txt', 'a') as women_file:
            women_file.write(w['name'] + "\n")


def get_bmi(mass, height):
    """Get bmi."""
    return float(mass.replace(',', '.')) / ((float(height.replace(',', '.')) / 100) ** 2)


def check_bmi(bmi):
    """Check bmi."""
    if bmi < 18.5:
        return 'niedowagę'
    elif bmi >= 25:
        return 'nadwagę'
    else:
        return 'normę'


def save_bmi(json_data):
    """Save persons with bmi."""
    filtered_data = list(
        filter(
            lambda a: a['mass'] != 'unknown' and a['height'] != 'unknown' and float(a['mass'].replace(',', '.')) > 0 and float(a['height'].replace(',', '.')) > 0,
            json_data))
    for person in filtered_data:
        bmi = get_bmi(person['mass'], person['height'])
        checked_bmi = check_bmi(bmi)
        tmp = "{0} wazy {1} kg, jest {2} i ma {3} \n"
        with open('sw_all_heroes.txt', 'a') as file:
            file.write(tmp.format(*[person['name'], person['mass'], person['gender'], checked_bmi]))


json_data = get_json_data_from_file('star_wars_data.json')
save_by_gender(json_data)
save_bmi(json_data)
