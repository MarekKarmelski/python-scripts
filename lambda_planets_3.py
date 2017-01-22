#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Lambda planets #3."""

from pprint import pprint as pp
from planets_data import get_planets_data


def lambda_planets_orbital_period():
    """Lambda function #3."""
    data = get_planets_data()
    current_data = list(
        filter(
            lambda a: a['surface_water'] is not 'unknown' and a['orbital_period'] is not 'unknown',
            data))
    min_orbital_period = min(current_data, key=lambda a: a['orbital_period'])
    max_orbital_period = max(current_data, key=lambda a: a['orbital_period'])
    print('MIN ORBITAL PERIOD')
    print('-' * 30)
    pp(min_orbital_period)
    print('MAX ORBITAL PERIOD')
    print('-' * 30)
    pp(max_orbital_period)

lambda_planets_orbital_period()