#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Lambda planets #6."""

from pprint import pprint as pp
from planets_data import get_planets_data


def lambda_planets_diameter_to_orbital_period():
    """Lambda function #6."""
    data = get_planets_data()
    current_data = list(
        filter(
            lambda a: a['diameter'] is not 'unknown' and a['diameter'] is not '0' and a['orbital_period'] is not 'unknown' and a['orbital_period'] is not '0', data))
    min_planet = min(current_data, key=lambda a: float(a['diameter'])/float(a['orbital_period']))
    print('PLANET')
    print('-' * 30)
    pp(min_planet)

lambda_planets_diameter_to_orbital_period()
