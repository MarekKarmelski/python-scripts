#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Lambda Star Wars #1."""

from pprint import pprint as pp
from star_wars_data import get_star_wars_data


def lambda_star_wars_sort_by_height():
    """Lambda function #1."""
    data = get_star_wars_data()
    sorted_by_height_sw_data = sorted(data, key=lambda a: a['height'], reverse=False)
    pp(sorted_by_height_sw_data)

lambda_star_wars_sort_by_height()
