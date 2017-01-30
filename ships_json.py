#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""JSON data."""

import json


def get_json_data_from_file(file_path):
    """Get JSON data from file."""
    with open(file_path) as json_file:
        data = json.load(json_file)
    return data


def save_ships_to_file(json_data):
    """Save ships to file."""
    filtered_data = list(filter(lambda a: a['cost_in_credits'] != 'unknown', json_data))
    sorted_by_cost = sorted(filtered_data, key=lambda a: float(a['cost_in_credits']), reverse=True)
    sentences = [ship['name'] + ' kosztuje ' + ship['cost_in_credits'] + ' credits' for ship in sorted_by_cost]
    for sentence in sentences:
        with open('sorted_ships.txt', 'a') as file:
            file.write(sentence + "\n")


json_data = get_json_data_from_file('ships.json')
save_ships_to_file(json_data)
