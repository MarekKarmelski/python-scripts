#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Lambda Star Wars #3."""

from pprint import pprint as pp
from star_wars_data import get_star_wars_data


def lambda_star_wars_min_max_bmi():
    """Lambda function #3."""
    data = get_star_wars_data()
    current_sw_data = list(filter(lambda a: a['height'] is not 'unknown' and a['mass'] is not 'unknown', data))
    min_bmi = min(current_sw_data,
                  key=lambda a: float(a['mass'].replace(',', '.')) / float(a['height'].replace(',', '.')) ** 2)
    max_bmi = max(current_sw_data,
                  key=lambda a: float(a['mass'].replace(',', '.')) / float(a['height'].replace(',', '.')) ** 2)
    print('MIN BMI')
    print('-'*30)
    pp(min_bmi)
    print('MAX BMI')
    print('-' * 30)
    pp(max_bmi)

lambda_star_wars_min_max_bmi()
