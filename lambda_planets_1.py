#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Lambda planets #1."""

from pprint import pprint as pp
from planets_data import get_planets_data


def lambda_planets_rotation_period():
    """Lambda function #1."""
    data = get_planets_data()
    sorted_by_rotation_period = sorted(data, key=lambda a: a['rotation_period'], reverse=False)
    pp(sorted_by_rotation_period)

lambda_planets_rotation_period()
