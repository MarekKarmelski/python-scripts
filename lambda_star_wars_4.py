#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Lambda Star Wars #4."""

from pprint import pprint as pp
from star_wars_data import get_star_wars_data


def lambda_star_wars_youngest_and_oldest():
    """Lambda function #4."""
    data = get_star_wars_data()
    current_sw_data = list(filter(lambda a: a['birth_year'] is not 'unknown', data))
    oldest = min(current_sw_data, key=lambda a: float(a['birth_year'].replace('BBY', '')) * -1)
    youngest = max(current_sw_data, key=lambda a: float(a['birth_year'].replace('BBY', '')) * -1)
    print('OLDEST')
    print('-' * 30)
    pp(oldest)
    print('YOUNGEST')
    print('-' * 30)
    pp(youngest)

lambda_star_wars_youngest_and_oldest()
