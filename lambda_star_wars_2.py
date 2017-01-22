#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Lambda Star Wars #2."""

from pprint import pprint as pp
from star_wars_data import get_star_wars_data


def lambda_star_wars_no_gender():
    """Lambda function #2."""
    data = get_star_wars_data()
    no_gender = list(filter(lambda a: a['gender'] == 'n/a', data))
    pp(no_gender)

lambda_star_wars_no_gender()
