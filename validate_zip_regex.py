#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Validate zip code using regular expression."""

import re


def validate_zip(zip_code):
    """Validate zip function."""
    match = re.search(
        r'^[0-9]{2}-[0-9]{3}$',
        zip_code
    )
    if match:
        return True
    else:
        return False

is_valid = validate_zip('11-222')
print(is_valid)