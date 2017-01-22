#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Lambda Star Wars #5."""

from pprint import pprint as pp
from star_wars_data import get_star_wars_data


def lambda_star_wars_aggregate_by_eye_color():
    """Lambda function #5."""
    data = get_star_wars_data()
    colors = set()
    for person in data:
        eye_color = person['eye_color'].split(', ')
        if len(eye_color) > 1:
            for c in eye_color:
                colors.add(c)
        else:
            colors.add(eye_color[0])

    data_by_eye_color = {}
    for color in colors:
        current_color = list(filter(lambda a: a['eye_color'].find(color) > -1, data))
        data_by_eye_color[color] = current_color
    pp(data_by_eye_color)

lambda_star_wars_aggregate_by_eye_color()
