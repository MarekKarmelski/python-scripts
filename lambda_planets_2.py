#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Lambda planets #2."""

from pprint import pprint as pp
from planets_data import get_planets_data


def lambda_planets_no_water():
    """Lambda function #2."""
    data = get_planets_data()
    no_water = list(filter(lambda a: a['surface_water'] == '0', data))
    pp(no_water)

lambda_planets_no_water()
