#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Lambda planets #4."""

from pprint import pprint as pp
from planets_data import get_planets_data
import math


def lambda_planets_smallest_and_biggest():
    """Lambda function #4."""
    data = get_planets_data()
    current_data = list(filter(lambda a: a['diameter'] is not 'unknown' and a['diameter'] is not '0', data))
    smallest_planet = min(current_data, key=lambda a: 4*math.pi*(float(a['diameter'])/2)**2)
    biggest_planet = max(current_data, key=lambda a: 4*math.pi*(float(a['diameter'])/2)**2)
    print('SMALLEST PLANET')
    print('-' * 30)
    pp(smallest_planet)
    print('BIGGEST PLANET')
    print('-' * 30)
    pp(biggest_planet)

lambda_planets_smallest_and_biggest()
