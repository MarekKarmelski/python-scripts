#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""BMI function with exceptions."""


def is_number(number):
    """Check if is number."""
    if isinstance(number, (float, int)):
        return number
    if not isinstance(number, str):
        return False
    number = number.replace(',', '.')
    try:
        return float(number)
    except ValueError:
        return False


def get_user_data():
    """User data function."""
    user_data = {}
    weight = is_number(input('Type weight: '))
    while weight is False:
        print('Weight is not number.')
        weight = is_number(input('Type weight: '))
    user_data['weight'] = weight
    height = is_number(input('Type height: '))
    while height is False:
        print('Height is not number.')
        height = is_number(input('Type height: '))
    user_data['height'] = height
    return user_data


def bmi():
    """BMI function."""
    user_data = get_user_data()
    bmi = round(user_data['weight'] / user_data['height'] ** 2, 2)
    print('Your BMI is: %s' % (bmi))

bmi()
